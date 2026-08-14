# AVCaptureEventPhase

**Framework**: AVKit  
**Kind**: enum

Constants that indicate the phase of a system capture event.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+

## Declaration

```swift
enum AVCaptureEventPhase
```

## Topics

### Creating a phase
- [init?(rawValue: UInt)](avcaptureeventphase/init(rawvalue:).md)
### Event phases
- [AVCaptureEventPhase.began](avcaptureeventphase/began.md)
  A phase that indicates the beginning of a capture event.
- [AVCaptureEventPhase.ended](avcaptureeventphase/ended.md)
  A phase that indicates the end of a capture event.
- [AVCaptureEventPhase.cancelled](avcaptureeventphase/cancelled.md)
  A phase that indicates the cancellation of a capture event.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var phase: AVCaptureEventPhase](avcaptureevent/phase.md)
  The current phase of a capture event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avkit/avcaptureeventphase)*