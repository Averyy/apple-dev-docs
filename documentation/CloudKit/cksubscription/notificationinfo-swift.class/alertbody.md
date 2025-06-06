# alertBody

**Framework**: CloudKit  
**Kind**: property

The text for the notification’s alert.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var alertBody: String? { get set }
```

#### Discussion

Set this property’s value to have the system display the specified string when it receives the corresponding push notification. If you localize your app’s content, use the [`alertLocalizationKey`](cksubscription/notificationinfo-swift.class/alertlocalizationkey.md) property instead.

## See Also

- [var alertLocalizationKey: String?](cksubscription/notificationinfo-swift.class/alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](cksubscription/notificationinfo-swift.class/alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](cksubscription/notificationinfo-swift.class/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](cksubscription/notificationinfo-swift.class/soundname.md)
  The filename of the sound file to play when a notification arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/alertbody)*