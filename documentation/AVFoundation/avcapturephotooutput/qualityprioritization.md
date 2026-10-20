# AVCapturePhotoOutput.QualityPrioritization

**Framework**: AVFoundation  
**Kind**: enum  
**Role**: Enumeration

Constants that indicate how to prioritize photo quality relative to capture speed.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- tvOS 17.0+

## Declaration

```swift
enum QualityPrioritization
```

```c
enum AVCapturePhotoQualityPrioritization : NSInteger;
```

## Topics

### Specifying priority
- [AVCapturePhotoOutput.QualityPrioritization.speed](./qualityprioritization/speed.md)
  Speed of photo delivery is most important, even at the expense of quality.
- [AVCapturePhotoOutput.QualityPrioritization.quality](./qualityprioritization/quality.md)
  Photo quality is most important, even at the expense of shot-to-shot time.
- [AVCapturePhotoOutput.QualityPrioritization.balanced](./qualityprioritization/balanced.md)
  Priority is balanced between photo quality and speed of delivery.
### Initializers
- [init?(rawValue: Int)](./qualityprioritization/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the capture prioritization
- [var maxPhotoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](./maxphotoqualityprioritization.md)
  The highest quality the photo output should prepare to deliver on a capture-by-capture basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/qualityprioritization)*