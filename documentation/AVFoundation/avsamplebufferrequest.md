# AVSampleBufferRequest

**Framework**: AVFoundation  
**Kind**: class

An object that describes a sample buffer creation request.

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
class AVSampleBufferRequest
```

## Topics

### Creating a request
- [init(start: AVSampleCursor)](avsamplebufferrequest/init(start:).md)
  Creates a newly allocated sample buffer request with the specified sample cursor.
### Configuring sample buffer request parameters
- [var direction: AVSampleBufferRequest.Direction](avsamplebufferrequest/direction-swift.property.md)
  The buffer sample direction.
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

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Playing custom audio with your own player](../AVFAudio/playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [class AVSampleBufferGenerator](avsamplebuffergenerator.md)
  An object that creates sample buffers.
- [class AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md)
  An object that generates sample buffers in a batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebufferrequest)*