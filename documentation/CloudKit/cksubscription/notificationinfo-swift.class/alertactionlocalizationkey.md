# alertActionLocalizationKey

**Framework**: CloudKit  
**Kind**: property

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

#### Discussion

Set this property’s value to have the system use a localized string for the text of the notification’s button that opens your app. The system uses the key to find the matching string in your app’s `Localizable.string` file.

If this property’s value is `nil`, the system displays a single button to dismiss the alert.

For information about localizing string resources, see [`Internationalization and Localization Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i).

## See Also

- [var alertBody: String?](cksubscription/notificationinfo-swift.class/alertbody.md)
  The text for the notification’s alert.
- [var alertLocalizationKey: String?](cksubscription/notificationinfo-swift.class/alertlocalizationkey.md)
  The key that identifies the localized string for the notification’s alert.
- [var alertLocalizationArgs: [CKRecord.FieldKey]?](cksubscription/notificationinfo-swift.class/alertlocalizationargs.md)
  The fields for building a notification’s alert.
- [var alertLaunchImage: String?](cksubscription/notificationinfo-swift.class/alertlaunchimage.md)
  The filename of an image to use as a launch image.
- [var soundName: String?](cksubscription/notificationinfo-swift.class/soundname.md)
  The filename of the sound file to play when a notification arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkit/cksubscription/notificationinfo-swift.class/alertactionlocalizationkey)*