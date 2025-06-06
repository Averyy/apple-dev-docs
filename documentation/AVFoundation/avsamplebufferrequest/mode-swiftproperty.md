# mode

**Framework**: AVFoundation  
**Kind**: property

The sample buffer request mode.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 10.10+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var mode: AVSampleBufferRequest.Mode { get set }
```

#### Discussion

Default is [`AVSampleBufferRequest.Mode.immediate`](avsamplebufferrequest/mode-swift.enum/immediate.md).

## See Also

- [var direction: AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.property.md)
  The buffer sample direction.
- [AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.enum.md)
  The modes that describe the buffer request direction.
- [var limitCursor: AVSampleCursor?](avsamplebufferrequest/limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](avsamplebufferrequest/maxsamplecount.md)
  The maximum number of samples to load.
- [AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.enum.md)
  The modes in which a sample buffer generator processes a request.
- [var overrideTime: CMTime](avsamplebufferrequest/overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](avsamplebufferrequest/preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](avsamplebufferrequest/startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.property)*