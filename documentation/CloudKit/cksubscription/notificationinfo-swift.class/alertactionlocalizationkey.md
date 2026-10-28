# alertActionLocalizationKey

**Framework**: CloudKit  
**Kind**: property  
**Role**: Instance Property

The key that identifies the localized string for the notification’s action.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
var alertActionLocalizationKey: String? { get set }
```

```objc
@property (copy, nullable) NSString * alertActionLocalizationKey;
```

## Discussion

Set this property’s value to have the system use a localized string for the text of the notification’s button that opens your app. The system uses the key to find the matching string in your app’s `Localizable.string` file.

If this property’s value is `nil`, the system displays a single button to dismiss the alert.

For information about localizing string resources, see [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## See Also

### Accessing the Notification Alert
- [var alertBody: String?](./alertbody.md)
  The text for the notification’s alert.
- [var alertLocalizationKey: String?](./alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](./alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertLaunchImage: String?](./alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](./soundname.md)
  The filename of the sound file to play when a notification arrives.
- [alertLocalizationArgs](../../cknotificationinfo/alertlocalizationargs.md)
  The fields for building a notification’s alert.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/alertactionlocalizationkey)*