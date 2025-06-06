# bracketSettings

**Framework**: AVFoundation  
**Kind**: property

The variations available for bracketed capture settings for this photo.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var bracketSettings: AVCaptureBracketedStillImageSettings? { get }
```

#### Discussion

When you request a bracketed capture using the [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md) class, you specify an array of [`AVCaptureBracketedStillImageSettings`](avcapturebracketedstillimagesettings.md) objects indicating the capture setting variations (such as exposure compensation) to apply to each image in the bracket. This property indicates the settings associated with this particular photo, or `nil` if this photo is not part of a bracketed capture.

## See Also

- [var sequenceCount: Int](avcapturephoto/sequencecount.md)
  The 1-based index of this photo in a bracketed capture sequence.
- [var lensStabilizationStatus: AVCaptureDevice.LensStabilizationStatus](avcapturephoto/lensstabilizationstatus.md)
  Information about the use of lens stabilization during bracketed photo capture.
- [AVCaptureDevice.LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md)
  Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/bracketsettings)*