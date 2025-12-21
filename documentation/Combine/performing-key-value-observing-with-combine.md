# Performing Key-Value Observing with Combine

**Framework**: Combine

Expose KVO changes with a Combine publisher.

#### Overview

Several frameworks use key-value observing to notify your app of asynchronous changes. By converting your use of KVO from callbacks and closures to Combine, you can make your code more elegant and maintainable.

##### Monitoring Changes with Kvo

In the following example, the type `UserInfo` supports KVO for its `lastLogin` property, as described in [`Using Key-Value Observing in Swift`](https://developer.apple.com/documentation/Swift/using-key-value-observing-in-swift). The [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) method uses the `observe(_:options:changeHandler:)` method to set up a closure that handles any change to the property. The closure receives an [`NSKeyValueObservedChange`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservedChange) object that describes the change event, retrieves the [`newValue`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservedChange/newValue) property, and prints it. The [`viewDidAppear(_:)`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidAppear(_:)) method changes the value, which calls the closure and prints the message.

```swift
class UserInfo: NSObject {
    @objc dynamic var lastLogin: Date = Date(timeIntervalSince1970: 0)
}
@objc var userInfo = UserInfo()
var observation: NSKeyValueObservation?

override func viewDidLoad() {
    super.viewDidLoad()
    observation = observe(\.userInfo.lastLogin, options: [.new]) { object, change in
        print ("lastLogin now \(change.newValue!).")
    }
}

override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    userInfo.lastLogin = Date()
}
```

##### Converting Kvo Code to Use Combine

To convert KVO code to Combine, replace the `observe(_:options:changeHandler:)` method with an [`NSObject.KeyValueObservingPublisher`](https://developer.apple.com/documentation/ObjectiveC/NSObject-swift.class/KeyValueObservingPublisher). You get an instance of this publisher by calling `publisher(for:)` on the parent object, as shown in the following example’s [`viewDidLoad()`](https://developer.apple.com/documentation/UIKit/UIViewController/viewDidLoad()) method:

```swift
class UserInfo: NSObject {
    @objc dynamic var lastLogin: Date = Date(timeIntervalSince1970: 0)
}
@objc var userInfo = UserInfo()
var cancellable: Cancellable?

override func viewDidLoad() {
    super.viewDidLoad()
    cancellable = userInfo.publisher(for: \.lastLogin)
        .sink() { date in print ("lastLogin now \(date).") }
}

override func viewDidAppear(_ animated: Bool) {
    super.viewDidAppear(animated)
    userInfo.lastLogin = Date()
}
```

The KVO publisher produces elements of the observed type — in this case, [`Date`](https://developer.apple.com/documentation/Foundation/Date) — rather than [`NSKeyValueObservedChange`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservedChange). This saves you a step, because you don’t have to unpack the [`newValue`](https://developer.apple.com/documentation/Foundation/NSKeyValueObservedChange/newValue) from the change object, as in the first example.

## See Also

- [Routing Notifications to Combine Subscribers](routing-notifications-to-combine-subscribers.md)
  Deliver notifications to subscribers by using notification centers’ publishers.
- [Replacing Foundation Timers with Timer Publishers](replacing-foundation-timers-with-timer-publishers.md)
  Publish elements periodically by using a timer.
- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)
  Apply common patterns to migrate your closure-based, event-handling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/performing-key-value-observing-with-combine)*