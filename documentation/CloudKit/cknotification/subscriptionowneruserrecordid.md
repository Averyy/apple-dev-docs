# subscriptionOwnerUserRecordID

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) CKRecordID * subscriptionOwnerUserRecordID;
```

## Discussion

On a system that supports multiple users, such as tvOS, use this identifier to check whether the pending content is for the current user. If your app always fetches data from CloudKit on launch, you may improve efficiency by disregarding notifications for other users.

For more information about supporting a multiuser environment, see [Personalizing Your App for Each User on Apple TV](../../TVServices/personalizing-your-app-for-each-user-on-apple-tv.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/subscriptionowneruserrecordid)*