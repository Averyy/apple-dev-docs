# alertLaunchImage

**Framework**: CloudKit  
**Kind**: property

The filename of an image to use as a launch image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var alertLaunchImage: String? { get }
```

#### Discussion

The system uses this property’s value to locate an image in the app’s bundle, and displays it as a launch image when the user launches the app after receiving a push notification.

## See Also

- [var alertBody: String?](cknotification/alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](cknotification/alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
- [var alertLocalizationArgs: [String]?](cknotification/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](cknotification/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var soundName: String?](cknotification/soundname.md)
  The name of the sound file to play when a notification arrives.
- [var badge: NSNumber?](cknotification/badge.md)
  The value that the app icon’s badge displays.
- [var category: String?](cknotification/category.md)
  The name of the action group that corresponds to this notification.
- [var subscriptionID: CKSubscription.ID?](cknotification/subscriptionid-16ygj.md)
  The ID of the subscription that triggers the notification.
- [var subscriptionOwnerUserRecordID: CKRecord.ID?](cknotification/subscriptionowneruserrecordid.md)
  The ID of the user record that creates the subscription that generates the push notification.
- [var title: String?](cknotification/title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](cknotification/titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [String]?](cknotification/titlelocalizationargs.md)
  The fields for building a notification’s title.
- [var subtitle: String?](cknotification/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](cknotification/subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [String]?](cknotification/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/alertlaunchimage)*