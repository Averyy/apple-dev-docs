# Routing Notifications to Combine Subscribers

**Framework**: Combine

Deliver notifications to subscribers by using notification centers’ publishers.

#### Overview

Many frameworks deliver asynchronous events to your app with the [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) API. Your app may already have places where it receives and processes these notifications in callback methods or closures. For example, the following code uses [`addObserver(forName:object:queue:using:)`](https://developer.apple.com/documentation/Foundation/NotificationCenter/addObserver(forName:object:queue:using:)) to print a message every time an iOS device rotates to portrait orientation.

```swift
var notificationToken: NSObjectProtocol?
override func viewDidLoad() {
    super.viewDidLoad()
    notificationToken = NotificationCenter.default
        .addObserver(forName: UIDevice.orientationDidChangeNotification,
                     object: nil,
                     queue: nil) { _ in
                        if UIDevice.current.orientation == .portrait {
                            print ("Orientation changed to portrait.")
                        }
    }
}
```

##### Migrate Notification Handling Code to Use Combine

Using notification center callbacks and closures requires you to do all your work inside the callback method or closure. By migrating to Combine, you can use operators to perform common tasks like filtering.

To take advantage of Combine, use the [`NotificationCenter.Publisher`](https://developer.apple.com/documentation/Foundation/NotificationCenter/Publisher) to migrate your [`NSNotification`](https://developer.apple.com/documentation/Foundation/NSNotification) handling code to the Combine idiom. You create this publisher with the [`NotificationCenter`](https://developer.apple.com/documentation/Foundation/NotificationCenter) method [`publisher(for:object:)`](https://developer.apple.com/documentation/Foundation/NotificationCenter/publisher(for:object:)), passing in the notification name in which you’re interested and a source object, if any.

Rewrite the above code in Combine as shown in the following listing. This code uses the default notification center to create a publisher for the [`orientationDidChangeNotification`](https://developer.apple.com/documentation/UIKit/UIDevice/orientationDidChangeNotification) notification. When the code receives notifications from this publisher, it applies a filter operator to only act on portrait orientation notifications, and prints a message.

```swift
var cancellable: Cancellable?
override func viewDidLoad() {
    super.viewDidLoad()
    cancellable = NotificationCenter.default
        .publisher(for: UIDevice.orientationDidChangeNotification)
        .filter() { _ in UIDevice.current.orientation == .portrait }
        .sink() { _ in print ("Orientation changed to portrait.") }
}
```

Note that in this case, the [`orientationDidChangeNotification`](https://developer.apple.com/documentation/UIKit/UIDevice/orientationDidChangeNotification) doesn’t contain the new orientation in its [`userInfo`](https://developer.apple.com/documentation/Foundation/Notification/userInfo) dictionary, so the [`filter(_:)`](publisher/filter(_:).md) operator queries the [`UIDevice`](https://developer.apple.com/documentation/UIKit/UIDevice) directly.

## See Also

- [Replacing Foundation Timers with Timer Publishers](replacing-foundation-timers-with-timer-publishers.md)
  Publish elements periodically by using a timer.
- [Performing Key-Value Observing with Combine](performing-key-value-observing-with-combine.md)
  Expose KVO changes with a Combine publisher.
- [Using Combine for Your App’s Asynchronous Code](using-combine-for-your-app-s-asynchronous-code.md)
  Apply common patterns to migrate your closure-based, event-handling code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/routing-notifications-to-combine-subscribers)*