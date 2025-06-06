# soundName

**Framework**: UIKit  
**Kind**: property

The name of the file containing the sound to play when an alert is displayed.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- watchOS 2.0+

## Declaration

```swift
@MainActor
var soundName: String? { get set }
```

#### Discussion

For this property, specify the filename (including extension) of a sound resource in the app’s main bundle or [`UILocalNotificationDefaultSoundName`](uilocalnotificationdefaultsoundname.md) to request the default system sound. When the system displays an alert for a local notification or badges an app icon, it plays this sound. The default value is `nil` (no sound). Sounds that last longer than 30 seconds are not supported. If you specify a file with a sound that plays over 30 seconds, the default sound is played instead.

For information on valid sound resources, see [`Registering, Scheduling, and Handling User Notifications`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/IPhoneOSClientImp.html#//apple_ref/doc/uid/TP40008194-CH103) in [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

- [var applicationIconBadgeNumber: Int](uilocalnotification/applicationiconbadgenumber.md)
  The number to display as the app’s icon badge.
- [var userInfo: [AnyHashable : Any]?](uilocalnotification/userinfo.md)
  A dictionary for passing custom information to the notified app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilocalnotification/soundname)*