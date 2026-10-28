# Performing Key-Value Observing with Combine

**Framework**: Combine  
**Role**: Article

Expose KVO changes with a Combine publisher.

## Overview

Several frameworks use key-value observing to notify your app of asynchronous changes. By converting your use of KVO from callbacks and closures to Combine, you can make your code more elegant and maintainable.

### Monitoring Changes with KVO

In the following example, the type `UserInfo` supports KVO for its `lastLogin` property, as described in [Using Key-Value Observing in Swift](../Swift/using-key-value-observing-in-swift.md). The [`viewDidLoad()`](../UIKit/uiviewcontroller/viewdidload%28%29.md) method uses the `observe(_:options:changeHandler:)` method to set up a closure that handles any change to the property. The closure receives an [`NSKeyValueObservedChange`](../Foundation/nskeyvalueobservedchange.md) object that describes the change event, retrieves the [`newValue`](../Foundation/nskeyvalueobservedchange/newvalue.md) property, and prints it. The [`viewDidAppear(_:)`](../UIKit/uiviewcontroller/viewdidappear%28_%29.md) method changes the value, which calls the closure and prints the message.

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

### Converting KVO Code to Use Combine

To convert KVO code to Combine, replace the `observe(_:options:changeHandler:)` method with an [`NSObject.KeyValueObservingPublisher`](../ObjectiveC/nsobject-swift.class/keyvalueobservingpublisher.md). You get an instance of this publisher by calling `publisher(for:)` on the parent object, as shown in the following example’s [`viewDidLoad()`](../UIKit/uiviewcontroller/viewdidload%28%29.md) method:

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

The KVO publisher produces elements of the observed type — in this case, [`Date`](../Foundation/date.md) — rather than [`NSKeyValueObservedChange`](../Foundation/nskeyvalueobservedchange.md). This saves you a step, because you don’t have to unpack the [`newValue`](../Foundation/nskeyvalueobservedchange/newvalue.md) from the change object, as in the first example.

## See Also

### Combine Migration
- [Routing Notifications to Combine Subscribers](./routing-notifications-to-combine-subscribers.md)
  Deliver notifications to subscribers by using notification centers’ publishers.
- [Replacing Foundation Timers with Timer Publishers](./replacing-foundation-timers-with-timer-publishers.md)
  Publish elements periodically by using a timer.
- [Using Combine for Your App’s Asynchronous Code](./using-combine-for-your-app-s-asynchronous-code.md)
  Apply common patterns to migrate your closure-based, event-handling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/performing-key-value-observing-with-combine)*