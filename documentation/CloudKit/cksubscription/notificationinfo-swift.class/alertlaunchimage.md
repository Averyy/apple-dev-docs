# alertLaunchImage

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The filename of an image to use as a launch image.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var alertLaunchImage: String? { get set }
```

```objc
@property (copy, nullable) NSString * alertLaunchImage;
```

## Discussion

If you specify a value, the system uses it to locate an image in the app’s bundle, and displays it as a launch image when the user launches the app after receiving a push notification.

## See Also

### Accessing the Notification Alert
- [var alertBody: String?](./alertbody.md)
  The text for the notification’s alert.
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](./alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertActionLocalizationKey: String?](./alertactionlocalizationkey.md)
  The key that identifies the localized string for the notification’s action.
- [var soundName: String?](./soundname.md)
  The filename of the sound file to play when a notification arrives.
- [alertLocalizationArgs](../../cknotificationinfo/alertlocalizationargs.md)
  The fields for building a notification’s alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/alertlaunchimage)*