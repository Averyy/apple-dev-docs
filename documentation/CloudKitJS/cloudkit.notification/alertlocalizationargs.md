# alertLocalizationArgs

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

An array of strings that appear as variables if [`alertLocalizationKey`](./alertlocalizationkey.md) is a format specifier.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute String[] alertLocalizationArgs;
```

#### Discussion

For details, read [Apple Push Notification Service](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/Chapters/ApplePushService.html#//apple_ref/doc/uid/TP40008194-CH100) in [Local and Remote Notification Programming Guide](https://developer.apple.com/library/archive/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/index.html#//apple_ref/doc/uid/TP40008194).

## See Also

### Presenting Notifications
- [alertActionLocalizationKey](./alertactionlocalizationkey.md)
  A key to get a localized right button title that appears in the alert dialog.
- [alertBody](./alertbody.md)
  The text of the alert message.
- [alertLaunchImage](./alertlaunchimage.md)
  The filename of an image file in the app bundle used as a launch image.
- [alertLocalizationKey](./alertlocalizationkey.md)
  A key to a localized alert message.
- [badge](./badge.md)
  The badge number to display.
- [category](./category.md)
  Name of the action group corresponding to this notification.
- [soundName](./soundname.md)
  The name of a sound file in the app bundle to play as an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notification/alertlocalizationargs)*