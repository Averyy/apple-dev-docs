# mode

**Framework**: AVFoundation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) AVSampleBufferRequestMode mode;
```

#### Discussion

Default is [`AVSampleBufferRequest.Mode.immediate`](./mode-swift.enum/immediate.md).

## See Also

### Configuring sample buffer request parameters
- [var direction: AVSampleBufferRequest.Direction](./direction-swift.property.md)
  The buffer sample direction.
- [AVSampleBufferRequest.Direction](./direction-swift.enum.md)
  The modes that describe the buffer request direction.
- [var limitCursor: AVSampleCursor?](./limitcursor.md)
  The limiting position for sample loading.
- [var maxSampleCount: Int](./maxsamplecount.md)
  The maximum number of samples to load.
- [AVSampleBufferRequest.Mode](./mode-swift.enum.md)
  The modes in which a sample buffer generator processes a request.
- [var overrideTime: CMTime](./overridetime.md)
  The deadline for sample data and output PTS for the sample buffer.
- [var preferredMinSampleCount: Int](./preferredminsamplecount.md)
  The preferred minimum number of samples to load.
- [var startCursor: AVSampleCursor](./startcursor.md)
  The starting cursor position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest/mode-swift.property)*