# didFinishLaunchingNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts immediately after the app finishes launching.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let didFinishLaunchingNotification: NSNotification.Name
```

#### Discussion

If the app was launched as a result of in remote notification targeted at it or because another app opened a URL resource claimed the posting app (the notification `object`), this notification contains a `userInfo` dictionary. You can access the contents of the dictionary using the [`url`](uiapplication/launchoptionskey/url.md) and [`sourceApplication`](uiapplication/launchoptionskey/sourceapplication.md) constants (for URLs), the [`remoteNotification`](uiapplication/launchoptionskey/remotenotification.md) constant (for remote notifications), and the [`localNotification`](uiapplication/launchoptionskey/localnotification.md) constant (for local notifications). If the notification was posted for a normal app launch, there is no `userInfo` dictionary.

## See Also

- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:willfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](uiapplicationdelegate/application(_:didfinishlaunchingwithoptions:).md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [UIApplication.LaunchOptionsKey](uiapplication/launchoptionskey.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didfinishlaunchingnotification)*