# videoQuality

**Framework**: UIKit  
**Kind**: property

The video recording and transcoding quality.

**Availability**:
- iOS 3.1+
- iPadOS 3.1+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var videoQuality: UIImagePickerController.QualityType { get set }
```

#### Discussion

The video quality setting specified by this property is used during video recording. It is also used whenever picking a recorded movie. Specifically, if the video quality setting is lower than the video quality of an existing movie, displaying that movie in the picker results in transcoding the movie to the lower quality.

The various video qualities are listed in the [`UIImagePickerController.QualityType`](uiimagepickercontroller/qualitytype.md) enumeration. The default value is [`UIImagePickerController.QualityType.typeMedium`](uiimagepickercontroller/qualitytype/typemedium.md). To capture or transcode a movie using a video quality other than the default value, you must set the quality explicitly.

This property is available only if the [`mediaTypes`](uiimagepickercontroller/mediatypes.md) property’s value array includes the `kUTTypeMovie` media type.

## See Also

- [class func availableMediaTypes(for: UIImagePickerController.SourceType) -> [String]?](uiimagepickercontroller/availablemediatypes(for:).md)
  Retrieves the available media types for the specified source type.
- [class func isSourceTypeAvailable(UIImagePickerController.SourceType) -> Bool](uiimagepickercontroller/issourcetypeavailable(_:).md)
  Queries whether the device supports picking media using the specified source type.
- [UIImagePickerController.QualityType](uiimagepickercontroller/qualitytype.md)
  Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.
- [var videoMaximumDuration: TimeInterval](uiimagepickercontroller/videomaximumduration.md)
  The maximum duration, in seconds, for a video recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/videoquality)*