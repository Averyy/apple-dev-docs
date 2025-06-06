# subscriptionOwnerUserRecordID

**Framework**: CloudKit  
**Kind**: property

The ID of the user record that creates the subscription that generates the push notification.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var subscriptionOwnerUserRecordID: CKRecord.ID? { get }
```

#### Discussion

On a system that supports multiple users, such as tvOS, use this identifier to check whether the pending content is for the current user. If your app always fetches data from CloudKit on launch, you may improve efficiency by disregarding notifications for other users.

For more information about supporting a multiuser environment, see [`Personalizing Your App for Each User on Apple TV`](https://developer.apple.com/documentation/TVServices/personalizing-your-app-for-each-user-on-apple-tv).

## See Also

- [var alertBody: String?](cknotification/alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](cknotification/alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
- [var alertLocalizationArgs: [String]?](cknotification/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](cknotification/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](cknotification/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](cknotification/soundname.md)
  The name of the sound file to play when a notification arrives.
- [var badge: NSNumber?](cknotification/badge.md)
  The value that the app icon’s badge displays.
- [var category: String?](cknotification/category.md)
  The name of the action group that corresponds to this notification.
- [var subscriptionID: CKSubscription.ID?](cknotification/subscriptionid-16ygj.md)
  The ID of the subscription that triggers the notification.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/subscriptionowneruserrecordid)*