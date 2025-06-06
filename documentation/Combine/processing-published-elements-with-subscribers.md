# Processing Published Elements with Subscribers

**Framework**: Combine

Apply back pressure to precisely control when publishers produce elements.

#### Overview

In Combine, a [`Publisher`](publisher.md) produces elements, and a [`Subscriber`](subscriber.md) acts on the elements it receives. However, a publisher can’t send elements until the subscriber attaches and asks for them. The subscriber also controls the rate at which the publisher delivers elements, by using the [`Subscribers.Demand`](subscribers/demand.md) type to indicate how many elements it can receive. A subscriber can indicate demand in either of two ways:

- By calling [`request(_:)`](subscription/request(_:).md) on the [`Subscription`](subscription.md) instance that the publisher provided when the subscriber first subscribed.
- By returning a new demand when the publisher calls the subscriber’s [`receive(_:)`](subscriber/receive(_:).md) method to deliver an element.

Demand is additive: If a subscriber has demanded two elements, and then requests `Subscribers.Demand(.max(3))`, the publisher’s unsatisfied demand is now five elements. If the publisher then sends an element, the unsatisfied demand decreases to four. Publishing elements is the only way to reduce unsatisfied demand; subscribers can’t request negative demand.

Many apps just use the operators [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) and [`assign(to:on:)`](publisher/assign(to:on:).md) to create the convenience subscriber types [`Subscribers.Sink`](subscribers/sink.md) and [`Subscribers.Assign`](subscribers/assign.md), respectively. These two subscribers issue a demand for [`unlimited`](subscribers/demand/unlimited.md) when they first attach to the publisher. Once a publisher has unlimited demand, there can be no further negotiation of demand between subscriber and publisher.

##### Consume Elements As the Publisher Produces Them

When a publisher has high or unlimited demand, it could send elements faster than a subscriber can process them. This scenario could lead to elements being dropped, or rapidly increasing memory pressure as elements fill a buffer while they await processing.

This scenario can occur if you use the convenience subscribers, because they demand an unlimited number of elements. Ensure that the closure you provide to [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) and the side-effects of [`assign(to:on:)`](publisher/assign(to:on:).md) adhere to the following traits:

- Don’t block the publisher.
- Don’t consume excessive memory by buffering elements.
- Don’t get overwhelmed and fail to process elements.

Fortunately, many commonly used publishers, such as publishers associated with user-interface elements, publish at a manageable rate. Other common publishers only produce a single element, like the URL Loading System’s [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher). It’s perfectly safe to use sink and assign subscribers with these publishers.

##### Apply Back Pressure with a Custom Subscriber

To control the rate at which the publisher sends elements to your subscriber, create a custom implementation of the [`Subscriber`](subscriber.md) protocol. Use your implementation to specify demands that you know your subscriber can keep up with. As the subscriber receives elements, it can request more by returning a new demand value to [`receive(_:)`](subscriber/receive(_:).md), or by calling [`request(_:)`](subscription/request(_:).md) on the subscription. With either, your subscriber can then fine-tune the number of elements the publisher can send it at any given time.

This concept of controlling flow by signaling a subscriber’s readiness to receive elements is called .

Each publisher keeps track of its current unsatisfied demand, meaning how many more elements a subscriber has requested. Even automated sources like Foundation’s [`Timer.TimerPublisher`](https://developer.apple.com/documentation/Foundation/Timer/TimerPublisher) only produce elements when they have pending demand. The following example code illustrates this behavior.

```swift
// Publisher: Uses a timer to emit the date once per second.
let timerPub = Timer.publish(every: 1, on: .main, in: .default)
    .autoconnect()

// Subscriber: Waits 5 seconds after subscription, then requests a
// maximum of 3 values.
class MySubscriber: Subscriber {
    typealias Input = Date
    typealias Failure = Never
    var subscription: Subscription?
    
    func receive(subscription: Subscription) {
        print("published                             received")
        self.subscription = subscription
        DispatchQueue.main.asyncAfter(deadline: .now() + 5) {
            subscription.request(.max(3))
        }
    }
    
    func receive(_ input: Date) -> Subscribers.Demand {
        print("\(input)             \(Date())")
        return Subscribers.Demand.none
    }
    
    func receive(completion: Subscribers.Completion<Never>) {
        print ("--done--")
    }
}

// Subscribe to timerPub.
let mySub = MySubscriber()
print ("Subscribing at \(Date())")
timerPub.subscribe(mySub)
```

The subscriber’s `receive(subscription:)` implementation uses a five-second delay before it requests any elements from the publisher. During this period, the publisher exists and has a valid subscriber, but has zero demand, so it doesn’t produce elements. It only starts publishing elements after the delay expires and the subscriber gives it a nonzero demand, as seen in the following output:

```text
Subscribing at 2019-12-09 18:57:06 +0000
published                             received
2019-12-09 18:57:11 +0000             2019-12-09 18:57:11 +0000
2019-12-09 18:57:12 +0000             2019-12-09 18:57:12 +0000
2019-12-09 18:57:13 +0000             2019-12-09 18:57:13 +0000
```

This example only requests three elements, issuing the demand after the five-second delay expires. As a result, the publisher sends no further elements after the third, but also doesn’t complete publishing by sending a [`Subscribers.Completion.finished`](subscribers/completion/finished.md) value either, because the publisher is just waiting for more demand. To continue to receive elements, the subscriber could store the subscription and periodically request more elements. It could also indicate new demand as the return value from its [`receive(_:)`](subscriber/receive(_:).md) implementation.

##### Manage Unlimited Demand By Using Back Pressure Operators

Even without writing a custom [`Subscriber`](subscriber.md), you can still apply back pressure by using one of Combine’s buffering or timing operators:

- [`buffer(size:prefetch:whenFull:)`](publisher/buffer(size:prefetch:whenfull:).md) holds onto a fixed number of items from an upstream publisher. When full, the buffer either drops elements or throws an error.
- [`debounce(for:scheduler:options:)`](publisher/debounce(for:scheduler:options:).md) publishes only when the upstream publisher stops publishing for a specified interval of time.
- [`throttle(for:scheduler:latest:)`](publisher/throttle(for:scheduler:latest:).md) produces elements at a given maximum rate. If it receives multiple elements during an interval, it sends only the newest or oldest.
- [`collect(_:)`](publisher/collect(_:).md) and [`collect(_:options:)`](publisher/collect(_:options:).md) bundle elements until they exceed a given count or time interval, sending you an array of elements. This option is good if your subscriber can process multiple elements at the same time.

Because these operators control the number of elements your subscriber receives, you can attach a subscriber that requests unlimited elements, such as [`sink(receiveValue:)`](publisher/sink(receivevalue:).md) and [`assign(to:on:)`](publisher/assign(to:on:).md).

## See Also

- [protocol Subscriber](subscriber.md)
  A protocol that declares a type that can receive input from a publisher.
- [enum Subscribers](subscribers.md)
  A namespace for types that serve as subscribers.
- [struct AnySubscriber](anysubscriber.md)
  A type-erasing subscriber.
- [protocol Subscription](subscription.md)
  A protocol representing the connection of a subscriber to a publisher.
- [enum Subscriptions](subscriptions.md)
  A namespace for symbols related to subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/processing-published-elements-with-subscribers)*