# alertLocalizationArgs

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The fields for building a notification’s alert.

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
var alertLocalizationArgs: [String]? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSString *> * alertLocalizationArgs;
```

#### Discussion

This property is an array of field names that CloudKit uses to extract the corresponding values from the record that triggers the push notification. The values are strings, numbers, or dates. CloudKit may truncate strings with a length greater than 100 characters when it adds them to a notification’s payload.

If you use `%@` for your substitution variables, CloudKit replaces those variables by traversing the array in order. If you use variables of the form `%n$@`, where `n` is an integer, `n` represents the index (starting at 1) of the item in the array to use. So, the first item in the array replaces the variable `%1$@`, the second item replaces the variable `%2$@`, and so on. You can use indexed substitution variables to change the order of items in the resulting string, which might be necessary when you localize your app’s content.

## See Also

### Accessing the Notification Info
- [var alertBody: String?](./alertbody.md)
  The notification’s alert body.
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized text for the alert body.
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

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/alertlocalizationargs)*