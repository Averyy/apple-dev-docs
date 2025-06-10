# maxPhotoQualityPrioritization

**Framework**: AVFoundation  
**Kind**: property

The highest quality the photo output should prepare to deliver on a capture-by-capture basis.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
var maxPhotoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization { get set }
```

#### Discussion

[`AVCapturePhotoOutput`](avcapturephotooutput.md) can apply a variety of techniques to improve photo quality, such as reducing noise, preserving detail in low light, freezing motion, and so on. Some techniques improve image quality at the expense of the shot-to-shot time. Before starting your session, you may set this property to indicate the highest quality prioritization you intend to request when calling the [`capturePhoto(with:delegate:)`](avcapturephotooutput/capturephoto(with:delegate:).md) method.

When configuring an [`AVCapturePhotoSettings`](avcapturephotosettings.md) object, you can’t exceed this quality prioritization level, but you may select a lower prioritization level that favors speed over quality.

When you attach the photo output to an [`AVCaptureSession`](avcapturesession.md), the default value of this property is [`AVCapturePhotoOutput.QualityPrioritization.balanced`](avcapturephotooutput/qualityprioritization/balanced.md). If you instead attach it to an [`AVCaptureMultiCamSession`](avcapturemulticamsession.md), the default value is [`AVCapturePhotoOutput.QualityPrioritization.speed`](avcapturephotooutput/qualityprioritization/speed.md).

> ❗ **Important**:  Changing the value of this property while the session is running causes the session to be rebuilt. This can be an expensive operation that will interrupt video preview until complete.

## See Also

- [AVCapturePhotoOutput.QualityPrioritization](avcapturephotooutput/qualityprioritization.md)
  Constants that indicate how to prioritize photo quality relative to capture speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxphotoqualityprioritization)*