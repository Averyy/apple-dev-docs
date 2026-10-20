# didFinishLaunchingNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that posts immediately after the app finishes launching.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
nonisolated
class let didFinishLaunchingNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIApplicationDidFinishLaunchingNotification;
```

#### Discussion

If the app was launched as a result of in remote notification targeted at it or because another app opened a URL resource claimed the posting app (the notification `object`), this notification contains a `userInfo` dictionary. You can access the contents of the dictionary using the [`url`](./launchoptionskey/url.md) and [`sourceApplication`](./launchoptionskey/sourceapplication.md) constants (for URLs), the [`remoteNotification`](./launchoptionskey/remotenotification.md) constant (for remote notifications), and the [`localNotification`](./launchoptionskey/localnotification.md) constant (for local notifications). If the notification was posted for a normal app launch, there is no `userInfo` dictionary.

## See Also

### Initializing the app
- [func application(UIApplication, willFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](../uiapplicationdelegate/application%28_,willfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process has begun.
- [func application(UIApplication, didFinishLaunchingWithOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool](../uiapplicationdelegate/application%28_,didfinishlaunchingwithoptions%29.md)
  Tells the delegate that the launch process is almost done and the app is almost ready to run.
- [UIApplication.LaunchOptionsKey](./launchoptionskey.md)
  The keys you use to access values in the launch options dictionary that the system passes to your app at initialization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/didfinishlaunchingnotification)*