# alertLocalizationArgs

**Framework**: CloudKit JS  
**Kind**: property

An array of strings that appear as variables if [`alertLocalizationKey`](cloudkit.notification/alertlocalizationkey.md) is a format specifier.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```swift
readonly attribute String[] alertLocalizationArgs;
```

#### Discussion

For details, read [`Apple Push Notification Service`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100) in [`Local and Remote Notification Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

- [alertActionLocalizationKey](cloudkit.notification/alertactionlocalizationkey.md)
  A key to get a localized right button title that appears in the alert dialog.
- [alertBody](cloudkit.notification/alertbody.md)
  The text of the alert message.
- [alertLaunchImage](cloudkit.notification/alertlaunchimage.md)
  The filename of an image file in the app bundle used as a launch image.
- [alertLocalizationKey](cloudkit.notification/alertlocalizationkey.md)
  A key to a localized alert message.
- [badge](cloudkit.notification/badge.md)
  The badge number to display.
- [category](cloudkit.notification/category.md)
  Name of the action group corresponding to this notification.
- [soundName](cloudkit.notification/soundname.md)
  The name of a sound file in the app bundle to play as an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notification/alertlocalizationargs)*