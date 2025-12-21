# Receiving and Handling Events with Combine

**Framework**: Combine

Customize and receive events from asynchronous sources.

#### Overview

The Combine framework provides a declarative approach for how your app processes events. Rather than potentially implementing multiple delegate callbacks or completion handler closures, you can create a single processing chain for a given event source. Each part of the chain is a Combine operator that performs a distinct action on the elements received from the previous step.

Consider an app that needs to filter a table or collection view based on the contents of a text field. In AppKit, each keystroke in the text field produces a [`Notification`](https://developer.apple.com/documentation/Foundation/Notification) that you can subscribe to with Combine. After receiving the notification, you can use operators to change the content and timing of event delivery, and use the final result to update your app’s user interface.

##### Connect a Publisher to a Subscriber

To receive the text field’s notifications with Combine, access the default instance of [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) and call its [`publisher(for:object:)`](https://developer.apple.com/documentation/Foundation/NotificationCenter/publisher(for:object:)) method. This call takes the notification name and source object that you want notifications from, and returns a publisher that produces notification elements.

```swift
let pub = NotificationCenter.default
    .publisher(for: NSControl.textDidChangeNotification, object: filterField)
```

You use a [`Subscriber`](subscriber.md) to receive elements from the publisher. The subscriber defines an associated type, [`Input`](subscriber/input.md), to declare the type that it receives. The publisher also defines a type, [`Output`](publisher/output.md), to declare what it produces. The publisher and subscriber both define a type, [`Failure`](publisher/failure.md), to indicate the kind of error they produce or receive. To connect a subscriber to a producer, the [`Output`](publisher/output.md) must match the [`Input`](subscriber/input.md), and the [`Failure`](publisher/failure.md) types must also match.

Combine provides two built-in subscribers, which automatically match the output and failure types of their attached publisher:

- [`sink(receiveCompletion:receiveValue:)`](publisher/sink(receivecompletion:receivevalue:).md) takes two closures. The first closure executes when it receives [`Subscribers.Completion`](subscribers/completion.md), which is an enumeration that indicates whether the publisher finished normally or failed with an error. The second closure executes when it receives an element from the publisher.
- [`assign(to:on:)`](publisher/assign(to:on:).md) immediately assigns every element it receives to a property of a given object, using a key path to indicate the property.

For example, you can use the sink subscriber to log when the publisher completes, and each time it receives an element:

```swift
let sub = NotificationCenter.default
    .publisher(for: NSControl.textDidChangeNotification, object: filterField)
    .sink(receiveCompletion: { print ($0) },
          receiveValue: { print ($0) })
```

Both the `sink(receiveCompletion:receiveValue:)` and [`assign(to:on:)`](publisher/assign(to:on:).md) subscribers request an unlimited number of elements from their publishers. To control the rate at which you receive elements, create your own subscriber by implementing the [`Subscriber`](subscriber.md) protocol.

##### Change the Output Type with Operators

The sink subscriber in the previous section performs all its work in the `receiveValue` closure. This could be burdensome if it needs to perform a lot of custom work with received elements or maintain state between invocations. The advantage of Combine comes from combining operators to customize event delivery.

For example, the [`NotificationCenter.Publisher`](https://developer.apple.com/documentation/Foundation/NotificationCenter/Publisher) provided by Foundation’s [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) uses [`Notification`](https://developer.apple.com/documentation/Foundation/Notification) as its [`Output`](publisher/output.md) type. This isn’t a convenient type to receive in the callback if what you need is the text field’s string value.

Since a publisher’s output is essentially a sequence of elements over time, Combine offers sequence-modifying operators like [`map(_:)`](publisher/map(_:)-99evh.md), [`flatMap(maxPublishers:_:)`](publisher/flatmap(maxpublishers:_:)-3k7z5.md), and [`reduce(_:_:)`](publisher/reduce(_:_:).md). The behavior of these operators is similar to their equivalents in the Swift standard library. To change the output type of the publisher, you add a [`map(_:)`](publisher/map(_:)-99evh.md) operator whose closure returns a different type. In this case, you can get the notification’s object as an [`NSTextField`](https://developer.apple.com/documentation/AppKit/NSTextField), and then get the field’s [`stringValue`](https://developer.apple.com/documentation/AppKit/NSControl/stringValue).

```swift
let sub = NotificationCenter.default
    .publisher(for: NSControl.textDidChangeNotification, object: filterField)
    .map( { ($0.object as! NSTextField).stringValue } )
    .sink(receiveCompletion: { print ($0) },
          receiveValue: { print ($0) })
```

After the publisher chain produces the type you want, replace `sink(receiveCompletion:receiveValue:)` with [`assign(to:on:)`](publisher/assign(to:on:).md). The following example takes the strings it receives from the publisher chain and assigns them to the `filterString` of a custom view model object:

```swift
let sub = NotificationCenter.default
    .publisher(for: NSControl.textDidChangeNotification, object: filterField)
    .map( { ($0.object as! NSTextField).stringValue } )
    .assign(to: \MyViewModel.filterString, on: myViewModel)
```

##### Customize Publishers with Operators

You can extend the [`Publisher`](publisher.md) instance with an operator that performs actions that you’d otherwise need to code manually. Here are three ways you could use operators to improve this event-processing chain:

- Rather than updating the view model with any string typed into the text field, you could use the [`filter(_:)`](publisher/filter(_:).md) operator to ignore input under a certain length or to reject non-alphanumeric characters.
- If the filtering operation is expensive — for example, if it’s querying a large database — you might want to wait for the user to stop typing. For this, the [`debounce(for:scheduler:options:)`](publisher/debounce(for:scheduler:options:).md) operator lets you set a minimum period of time that must elapse before a publisher emits an event. The [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop) class provides conveniences for specifying the time delay in seconds or milliseconds.
- If the results update the UI, you can deliver callbacks to the main thread by calling the [`receive(on:options:)`](publisher/receive(on:options:).md) method. By specifying the [`Scheduler`](scheduler.md) instance provided by the [`RunLoop`](https://developer.apple.com/documentation/Foundation/RunLoop) class as the first parameter, you tell Combine to call your subscriber on the main run loop.

The resulting publisher declaration follows:

```swift
let sub = NotificationCenter.default
    .publisher(for: NSControl.textDidChangeNotification, object: filterField)
    .map( { ($0.object as! NSTextField).stringValue } )
    .filter( { $0.unicodeScalars.allSatisfy({CharacterSet.alphanumerics.contains($0)}) } )
    .debounce(for: .milliseconds(500), scheduler: RunLoop.main)
    .receive(on: RunLoop.main)
    .assign(to:\MyViewModel.filterString, on: myViewModel)
```

##### Cancel Publishing When Desired

A publisher continues to emit elements until it completes normally or fails. If you no longer want to subscribe to the publisher, you can cancel the subscription. The subscriber types created by `sink(receiveCompletion:receiveValue:)` and [`assign(to:on:)`](publisher/assign(to:on:).md) both implement the [`Cancellable`](cancellable.md) protocol, which provides a [`cancel()`](cancellable/cancel().md) method:

```swift
sub?.cancel()
```

If you create a custom [`Subscriber`](subscriber.md), the publisher sends a [`Subscription`](subscription.md) object when you first subscribe to it. Store this subscription, and then call its [`cancel()`](cancellable/cancel().md) method when you want to cancel publishing. When you create a custom subscriber, you should implement the [`Cancellable`](cancellable.md) protocol, and have your [`cancel()`](cancellable/cancel().md) implementation forward the call to the stored subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/receiving-and-handling-events-with-combine)*