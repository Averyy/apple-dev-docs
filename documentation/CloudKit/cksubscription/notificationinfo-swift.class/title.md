# title

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The notification’s title.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var title: String? { get set }
```

```objc
@property (copy, nullable) NSString * title;
```

#### Discussion

CloudKit uses this value to set the `title` push notification property.

See [Generating a remote notification](../../../UserNotifications/generating-a-remote-notification.md) for more detail about push notification properties.

## See Also

### Accessing the Notification Title
- [var titleLocalizationKey: String?](./titlelocalizationkey.md)
  The key that identifies the localized string for the notification’s title.
- [var titleLocalizationArgs: [CKRecord.FieldKey]?](./titlelocalizationargs.md)
  The fields for building a notification’s title.
- [titleLocalizationArgs](../../cknotificationinfo/titlelocalizationargs.md)
  The fields for building a notification’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/title)*