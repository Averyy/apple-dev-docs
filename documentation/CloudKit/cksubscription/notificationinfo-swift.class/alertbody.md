# alertBody

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (copy, nullable) NSString * alertBody;
```

#### Discussion

Set this property’s value to have the system display the specified string when it receives the corresponding push notification. If you localize your app’s content, use the [`alertLocalizationKey`](./alertlocalizationkey.md) property instead.

## See Also

### Accessing the Notification Alert
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](./alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](./alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](./soundname.md)
  The filename of the sound file to play when a notification arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/alertbody)*