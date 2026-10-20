# category

**Framework**: CloudKit JS  
**Kind**: property  
**Role**: Instance Property

Name of the action group corresponding to this notification.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
readonly attribute String category;
```

#### Discussion

Categories of actions allow you to present custom actions to the user on your push notifications. For details, see [`UIUserNotificationCategory`](../../UIKit/uiusernotificationcategory.md).

## See Also

### Presenting Notifications
- [alertActionLocalizationKey](./alertactionlocalizationkey.md)
  A key to get a localized right button title that appears in the alert dialog.
- [alertBody](./alertbody.md)
  The text of the alert message.
- [alertLaunchImage](./alertlaunchimage.md)
  The filename of an image file in the app bundle used as a launch image.
- [alertLocalizationArgs](./alertlocalizationargs.md)
  An array of strings that appear as variables if [`alertLocalizationKey`](./alertlocalizationkey.md) is a format specifier.
- [alertLocalizationKey](./alertlocalizationkey.md)
  A key to a localized alert message.
- [badge](./badge.md)
  The badge number to display.
- [soundName](./soundname.md)
  The name of a sound file in the app bundle to play as an alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.notification/category)*