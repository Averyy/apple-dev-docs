# alertActionLocalizationKey

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The key that identifies the localized string for the notification’s action.

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
var alertActionLocalizationKey: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * alertActionLocalizationKey;
```

#### Discussion

The system uses this property’s value to find the matching string in your app’s `Localizable.strings` file. It uses the string as the text of the button that opens your app, which the notification alert displays.

If this property’s value is `nil`, the system displays a single button to dismiss the alert.

## See Also

### Accessing the Notification Info
- [var alertBody: String?](./alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
- [var alertLocalizationArgs: [String]?](./alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  The filename of an image to use as a launch image.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/alertactionlocalizationkey)*