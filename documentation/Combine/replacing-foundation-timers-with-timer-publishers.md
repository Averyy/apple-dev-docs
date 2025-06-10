# Replacing Foundation Timers with Timer Publishers

**Framework**: Combine

Publish elements periodically by using a timer.

#### Overview

If your app uses Foundation’s [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) class to repeatedly receive a callback or invoke a closure on a specified interval, you can convert these instances to Combine to simplify your code.

##### Performing Periodic Work with a Timer

Consider the following snippet, which uses [`scheduledTimer(withTimeInterval:repeats:block:)`](https://developer.apple.com/documentation/Foundation/Timer/scheduledTimer(withTimeInterval:repeats:block:)) to update the `lastUpdated` property of a data model once a second, on a specific dispatch queue:

```swift
var timer: Timer?
override func viewDidLoad() {
    super.viewDidLoad()
    timer = Timer.scheduledTimer(withTimeInterval: 1, repeats: true) { _ in
        self.myDispatchQueue.async() {
            self.myDataModel.lastUpdated = Date()
        }
    }
}
```

##### Converting to a Timer Publisher

To migrate this code to Combine, replace the [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) that is returned by [`scheduledTimer(withTimeInterval:repeats:block:)`](https://developer.apple.com/documentation/Foundation/Timer/scheduledTimer(withTimeInterval:repeats:block:)) with a [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher). You create this publisher with the [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) method [`publish(every:tolerance:on:in:options:)`](https://developer.apple.com/documentation/Foundation/Timer/publish(every:tolerance:on:in:options:)). Every time the underyling [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) fires, the publisher emits a new [`Date`](https://developer.apple.com/documentation/Foundation/Date) that represents the instant the timer fired. You then apply Combine operators to the [`Date`](https://developer.apple.com/documentation/Foundation/Date), eventually connecting the publisher to a subscriber like [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) or [`assign(to:on:)`](publisher/assign(to:on:).md).

> 💡 **Tip**: Because [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) conforms to the [`ConnectablePublisher`](connectablepublisher.md) protocol, it won’t produce elements until you explicitly connect to it. Do this by either calling [`connect()`](connectablepublisher/connect().md), or using an [`autoconnect()`](connectablepublisher/autoconnect().md) operator to connect automatically when a subscriber attaches.

The next example shows how to use a [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) to replace the previous example. It uses Combine’s operators to perform the tasks that were in the previous example’s closure:

```swift
var cancellable: Cancellable?
override func viewDidLoad() {
    super.viewDidLoad()
    cancellable = Timer.publish(every: 1, on: .main, in: .default)
        .autoconnect()
        .receive(on: myDispatchQueue)
        .assign(to: \.lastUpdated, on: myDataModel)
}
```

In this example, Combine operators replace all the behavior inside the closure of the earlier example:

- The [`receive(on:options:)`](publisher/receive(on:options:).md) operator ensures that its subsequent operators run on the specified dispatch queue. This replaces the `async()` call from before.
- The [`assign(to:on:)`](publisher/assign(to:on:).md) operator updates the data model, by using a key path to set the `lastUpdate` property.

Another advantage you’ll find when using Combine to simplify your code is that the [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) produces new [`Date`](https://developer.apple.com/documentation/Foundation/Date) instances as its output type. The first example’s closure receives the [`Timer`](https://developer.apple.com/documentation/Foundation/Timer) itself as its parameter, so it has to create new [`Date`](https://developer.apple.com/documentation/Foundation/Date) instances manually.

## See Also

- [Routing Notifications to Combine Subscribers](routing-notifications-to-combine-subscribers.md)
  Deliver notifications to subscribers by using notification centers’ publishers.
- [Performing Key-Value Observing with Combine](performing-key-value-observing-with-combine.md)
  Expose KVO changes with a Combine publisher.
- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)
  Apply common patterns to migrate your closure-based, event-handling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/replacing-foundation-timers-with-timer-publishers)*