# Replacing Foundation Timers with Timer Publishers

**Framework**: Combine  
**Role**: Article

Publish elements periodically by using a timer.

#### Overview

If your app uses Foundation’s [`Timer`](../Foundation/timer.md) class to repeatedly receive a callback or invoke a closure on a specified interval, you can convert these instances to Combine to simplify your code.

##### Performing Periodic Work with a Timer

Consider the following snippet, which uses [`scheduledTimer(withTimeInterval:repeats:block:)`](../Foundation/timer/scheduledtimer%28withtimeinterval,repeats,block%29.md) to update the `lastUpdated` property of a data model once a second, on a specific dispatch queue:

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

To migrate this code to Combine, replace the [`Timer`](../Foundation/timer.md) that is returned by [`scheduledTimer(withTimeInterval:repeats:block:)`](../Foundation/timer/scheduledtimer%28withtimeinterval,repeats,block%29.md) with a [`Timer.TimerPublisher`](../Foundation/timer/timerpublisher.md). You create this publisher with the [`Timer`](../Foundation/timer.md) method [`publish(every:tolerance:on:in:options:)`](../Foundation/timer/publish%28every,tolerance,on,in,options%29.md). Every time the underyling [`Timer`](../Foundation/timer.md) fires, the publisher emits a new [`Date`](../Foundation/date.md) that represents the instant the timer fired. You then apply Combine operators to the [`Date`](../Foundation/date.md), eventually connecting the publisher to a subscriber like [`sink(receiveValue:)`](./publisher/sink%28receivevalue%29.md) or [`assign(to:on:)`](./publisher/assign%28to,on%29.md).

> 💡 **Tip**: Because [`Timer.TimerPublisher`](../Foundation/timer/timerpublisher.md) conforms to the [`ConnectablePublisher`](./connectablepublisher.md) protocol, it won’t produce elements until you explicitly connect to it. Do this by either calling [`connect()`](./connectablepublisher/connect%28%29.md), or using an [`autoconnect()`](./connectablepublisher/autoconnect%28%29.md) operator to connect automatically when a subscriber attaches.

The next example shows how to use a [`Timer.TimerPublisher`](../Foundation/timer/timerpublisher.md) to replace the previous example. It uses Combine’s operators to perform the tasks that were in the previous example’s closure:

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

- The [`receive(on:options:)`](./publisher/receive%28on,options%29.md) operator ensures that its subsequent operators run on the specified dispatch queue. This replaces the `async()` call from before.
- The [`assign(to:on:)`](./publisher/assign%28to,on%29.md) operator updates the data model, by using a key path to set the `lastUpdate` property.

Another advantage you’ll find when using Combine to simplify your code is that the [`Timer.TimerPublisher`](../Foundation/timer/timerpublisher.md) produces new [`Date`](../Foundation/date.md) instances as its output type. The first example’s closure receives the [`Timer`](../Foundation/timer.md) itself as its parameter, so it has to create new [`Date`](../Foundation/date.md) instances manually.

## See Also

### Combine Migration
- [Routing Notifications to Combine Subscribers](./routing-notifications-to-combine-subscribers.md)
  Deliver notifications to subscribers by using notification centers’ publishers.
- [Performing Key-Value Observing with Combine](./performing-key-value-observing-with-combine.md)
  Expose KVO changes with a Combine publisher.
- [Using Combine for Your App’s Asynchronous Code](./using-combine-for-your-app-s-asynchronous-code.md)
  Apply common patterns to migrate your closure-based, event-handling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/replacing-foundation-timers-with-timer-publishers)*