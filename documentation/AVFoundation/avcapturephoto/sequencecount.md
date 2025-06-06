# sequenceCount

**Framework**: AVFoundation  
**Kind**: property

The 1-based index of this photo in a bracketed capture sequence.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 14.0+
- tvOS 17.0+

## Declaration

```swift
var sequenceCount: Int { get }
```

#### Discussion

If this photo is part of a bracketed capture (requested with the [`AVCapturePhotoBracketSettings`](avcapturephotobracketsettings.md) class), this property indicates the current result’s count in the sequence, starting with `1` for the first result.

If this photo is not part of a bracketed capture, this property’s value is `0`.

## See Also

- [var bracketSettings: AVCaptureBracketedStillImageSettings?](avcapturephoto/bracketsettings.md)
  The variations available for bracketed capture settings for this photo.
- [var lensStabilizationStatus: AVCaptureDevice.LensStabilizationStatus](avcapturephoto/lensstabilizationstatus.md)
  Information about the use of lens stabilization during bracketed photo capture.
- [AVCaptureDevice.LensStabilizationStatus](avcapturedevice/lensstabilizationstatus.md)
  Constants that indicate the status of optical image stabilization hardware during a bracketed photo capture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephoto/sequencecount)*