# titleLocalizationArgs

**Framework**: CloudKit  
**Kind**: property

The fields for building a notification’s title.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var titleLocalizationArgs: [String]? { get }
```

#### Discussion

This property is an array of field names that CloudKit uses to extract the corresponding values from the record that triggers the push notification. The values are strings, numbers, or dates. CloudKit may truncate strings with a length greater than 100 characters when it adds them to a notification’s payload.

If you use `%@` for your substitution variables, CloudKit replaces those variables by traversing the array in order. If you use variables of the form `%n$@`, where `n` is an integer, `n` represents the index (starting at 1) of the item in the array to use. So, the first item in the array replaces the variable `%1$@`, the second item replaces the variable `%2$@`, and so on. You can use indexed substitution variables to change the order of items in the resulting string, which might be necessary when you localize your app’s content.

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
- [var subscriptionOwnerUserRecordID: CKRecord.ID?](cknotification/subscriptionowneruserrecordid.md)
  The ID of the user record that creates the subscription that generates the push notification.
- [var title: String?](cknotification/title.md)
  The notification’s title.
- [var titleLocalizationKey: String?](cknotification/titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var subtitle: String?](cknotification/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationKey: String?](cknotification/subtitlelocalizationkey.md)
  The key that identifies the localized string for the notification’s subtitle.
- [var subtitleLocalizationArgs: [String]?](cknotification/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cknotification/titlelocalizationargs)*