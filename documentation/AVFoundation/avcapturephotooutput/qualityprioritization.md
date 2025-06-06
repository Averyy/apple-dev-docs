# AVCapturePhotoOutput.QualityPrioritization

**Framework**: AVFoundation  
**Kind**: enum

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

## Topics

### Specifying Priority
- [AVCapturePhotoOutput.QualityPrioritization.speed](avcapturephotooutput/qualityprioritization/speed.md)
  Speed of photo delivery is most important, even at the expense of quality.
- [AVCapturePhotoOutput.QualityPrioritization.quality](avcapturephotooutput/qualityprioritization/quality.md)
  Photo quality is most important, even at the expense of shot-to-shot time.
- [AVCapturePhotoOutput.QualityPrioritization.balanced](avcapturephotooutput/qualityprioritization/balanced.md)
  Priority is balanced between photo quality and speed of delivery.
### Initializers
- [init?(rawValue: Int)](avcapturephotooutput/qualityprioritization/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var maxPhotoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization](avcapturephotooutput/maxphotoqualityprioritization.md)
  The highest quality the photo output should prepare to deliver on a capture-by-capture basis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/qualityprioritization)*