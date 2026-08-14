# AVSampleBufferGeneratorBatch

**Framework**: AVFoundation  
**Kind**: class

An object that generates sample buffers in a batch.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
class AVSampleBufferGeneratorBatch
```

#### Overview

The benefit of batching is it aggregates adjacent I/O requests and overlaps them when possible for all sample buffers within the batch.

## Topics

### Preparing a batch
- [func makeDataReady(completionHandler: ((any Error)?) -> Void)](avsamplebuffergeneratorbatch/makedataready(completionhandler:).md)
  Loads sample data asynchronously for all sample buffers within a batch.
### Canceling a batch
- [func cancel()](avsamplebuffergeneratorbatch/cancel.md)
  Cancels any I/O for this batch.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [Playing custom audio with your own player](../avfaudio/playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [class AVSampleBufferRequest](avsamplebufferrequest.md)
  An object that describes a sample buffer creation request.
- [class AVSampleBufferGenerator](avsamplebuffergenerator.md)
  An object that creates sample buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergeneratorbatch)*