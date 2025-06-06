# videoMaximumDuration

**Framework**: UIKit  
**Kind**: property

The maximum duration, in seconds, for a video recording.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var videoMaximumDuration: TimeInterval { get set }
```

#### Discussion

The default value for this property is 10 minutes (600 seconds). When a user taps the Share button to send a movie to MMS, MobileMe, YouTube, or another destination, an appropriate duration limit and an appropriate video quality are enforced.

This property is available only if the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) property’s value array includes the `kUTTypeMovie` media type.

## See Also

- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](uiimagepickercontroller/availablemediatypes(for:).md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [var videoQuality: UIImagePickerController.QualityType](uiimagepickercontroller/videoquality.md)
  The video recording and transcoding quality.
- [UIImagePickerController.QualityType](uiimagepickercontroller/qualitytype.md)
  Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videomaximumduration)*