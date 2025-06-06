# subtitleLocalizationKey

**Framework**: CloudKit  
**Kind**: property

The key that identifies the localized string for the notification’s subtitle.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var subtitleLocalizationKey: String? { get set }
```

#### Discussion

CloudKit uses this value to set the `subtitle-loc-key` push notification property. Setting this property overrides any value in [`subtitle`](cksubscription/notificationinfo-swift.class/subtitle.md).

See [`Generating a remote notification`](https://developer.apple.com/documentation/UserNotifications/generating-a-remote-notification) for more details about push notification properties.

## See Also

- [var subtitle: String?](cksubscription/notificationinfo-swift.class/subtitle.md)
  The notification’s subtitle.
- [var subtitleLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/subtitlelocalizationargs.md)
  The fields for building a notification’s subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/subtitlelocalizationkey)*