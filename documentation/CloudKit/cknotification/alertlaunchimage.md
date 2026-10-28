# alertLaunchImage

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The filename of an image to use as a launch image.

**Availability**:
- iOS 8.0+ - Deprecated in 17.0
- iPadOS 8.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- macOS 10.10+ - Deprecated in 14.0
- visionOS 1.0+ - Deprecated in 1.0
- watchOS 3.0+ - Deprecated in 10.0

> **Deprecated**: Interact with UI elements of a CloudKit-server-generated push message via UserNotifications.framework

## Declaration

```swift
var alertLaunchImage: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * alertLaunchImage;
```

## Discussion

The system uses this property’s value to locate an image in the app’s bundle, and displays it as a launch image when the user launches the app after receiving a push notification.

## See Also

### Accessing the Notification Info
- [var alertBody: String?](./alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
- [var alertLocalizationArgs: [String]?](./alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](./alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var soundName: String?](./soundname.md)
  The name of the sound file to play when a notification arrives.
- [var badge: NSNumber?](./badge.md)
  The value that the app icon’s badge displays.
- [var category: String?](./category.md)
  The name of the action group that corresponds to this notification.
- [var subscriptionID: CKSubscription.ID?](./subscriptionid-16ygj.md)
  The ID of the subscription that triggers the notification.
- [var subscriptionOwnerUserRecordID: CKRecord.ID?](./subscriptionowneruserrecordid.md)
  The ID of the user record that creates the subscription that generates the push notification.
- [var title: String?](./title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](./titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [String]?](./titlelocalizationargs.md)
  The fields for building a notification’s title.
- [var subtitle: String?](./subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](./subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [String]?](./subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.
- [subscriptionID](./subscriptionid-90zhj.md)
  The ID of the subscription that triggers the notification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/alertlaunchimage)*