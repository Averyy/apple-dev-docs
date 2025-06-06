# titleLocalizationKey

**Framework**: CloudKit  
**Kind**: property

The key that identifies the localized string for the notification’s title.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var titleLocalizationKey: String? { get set }
```

#### Discussion

CloudKit uses this value to set the `title-loc-key` push notification property.

See [`Generating a remote notification`](https://developer.apple.com/documentation/UserNotifications/generating-a-remote-notification) for more details about push notification properties.

## See Also

- [var title: String?](cksubscription/notificationinfo-swift.class/title.md)
  The notification’s title.
- [var titleLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/titlelocalizationargs.md)
  The fields for building a notification’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/titlelocalizationkey)*