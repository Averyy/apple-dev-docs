# maxPhotoQualityPrioritization

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic) AVCapturePhotoQualityPrioritization maxPhotoQualityPrioritization;
```

#### Discussion

[`AVCapturePhotoOutput`](../avcapturephotooutput.md) can apply a variety of techniques to improve photo quality, such as reducing noise, preserving detail in low light, freezing motion, and so on. Some techniques improve image quality at the expense of the shot-to-shot time. Before starting your session, you may set this property to indicate the highest quality prioritization you intend to request when calling the [`capturePhoto(with:delegate:)`](./capturephoto%28with,delegate%29.md) method.

When configuring an [`AVCapturePhotoSettings`](../avcapturephotosettings.md) object, you can’t exceed this quality prioritization level, but you may select a lower prioritization level that favors speed over quality.

When you attach the photo output to an [`AVCaptureSession`](../avcapturesession.md), the default value of this property is [`AVCapturePhotoOutput.QualityPrioritization.balanced`](./qualityprioritization/balanced.md). If you instead attach it to an [`AVCaptureMultiCamSession`](../avcapturemulticamsession.md), the default value is [`AVCapturePhotoOutput.QualityPrioritization.speed`](./qualityprioritization/speed.md).

> ❗ **Important**:  Changing the value of this property while the session is running causes the session to be rebuilt. This can be an expensive operation that will interrupt video preview until complete.

## See Also

### Setting the capture prioritization
- [AVCapturePhotoOutput.QualityPrioritization](./qualityprioritization.md)
  Constants that indicate how to prioritize photo quality relative to capture speed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/maxphotoqualityprioritization)*