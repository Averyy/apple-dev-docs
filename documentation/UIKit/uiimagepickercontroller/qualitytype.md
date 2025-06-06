# UIImagePickerController.QualityType

**Framework**: UIKit  
**Kind**: enum

Constants that describe video quality settings for movies that are recorded with the built-in camera, or that are transcoded when they’re displayed in the image picker.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+

## Declaration

```swift
enum QualityType
```

#### Overview

The constants in this enumeration are for use as values of the [`videoQuality`](uiimagepickercontroller/videoquality.md) property.

The video quality setting applies to transcoding as well as to recording. Specifically, if the video quality setting is lower than the video quality of an existing movie, displaying that movie in the picker results in transcoding the movie to the lower quality.

## Topics

### Constants
- [UIImagePickerController.QualityType.typeHigh](uiimagepickercontroller/qualitytype/typehigh.md)
  If recording, specifies that you want to use the highest-quality video recording supported for the active camera on the device.
- [UIImagePickerController.QualityType.type640x480](uiimagepickercontroller/qualitytype/type640x480.md)
  If recording, specifies that you want to use VGA-quality video recording (pixel dimensions of 640x480).
- [UIImagePickerController.QualityType.typeMedium](uiimagepickercontroller/qualitytype/typemedium.md)
  If recording, specifies that you want to use medium-quality video recording.
- [UIImagePickerController.QualityType.typeLow](uiimagepickercontroller/qualitytype/typelow.md)
  If recording, specifies that you want to use low-quality video recording.
- [UIImagePickerController.QualityType.typeIFrame1280x720](uiimagepickercontroller/qualitytype/typeiframe1280x720.md)
  If recording, specifies that you want to use 1280x720 iFrame format.
- [UIImagePickerController.QualityType.typeIFrame960x540](uiimagepickercontroller/qualitytype/typeiframe960x540.md)
  If recording, specifies that you want to use 960x540 iFrame format.
### Initializers
- [init?(rawValue: Int)](uiimagepickercontroller/qualitytype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var videoQuality: UIImagePickerController.QualityType](uiimagepickercontroller/videoquality.md)
  The video recording and transcoding quality.
- [var videoMaximumDuration: TimeInterval](uiimagepickercontroller/videomaximumduration.md)
  The maximum duration, in seconds, for a video recording.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiimagepickercontroller/qualitytype)*