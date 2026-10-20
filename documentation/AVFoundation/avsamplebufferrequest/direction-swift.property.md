# direction

**Framework**: AVFoundation  
**Kind**: property

The buffer sample direction.

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
var direction: AVSampleBufferRequest.Direction { get set }
```

#### Discussion

The default value is [`AVSampleBufferRequest.Direction.none`](avsamplebufferrequest/direction-swift.enum/none.md).

## See Also

- [AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.enum.md)
  The modes that describe the buffer request direction.
- [var limitCursor: AVSampleCursor?](avsamplebufferrequest/limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](avsamplebufferrequest/maxsamplecount.md)
  The maximum number of samples to load.
- [var mode: AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.property.md)
  The sample buffer request mode.
- [AVSampleBufferRequest.Mode](avsamplebufferrequest/mode-swift.enum.md)
  The modes in which a sample buffer generator processes a request.
- [var overrideTime: CMTime](avsamplebufferrequest/overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](avsamplebufferrequest/preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](avsamplebufferrequest/startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/direction-swift.property)*