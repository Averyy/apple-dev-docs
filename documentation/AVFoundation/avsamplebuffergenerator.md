# AVSampleBufferGenerator

**Framework**: AVFoundation  
**Kind**: class

An object that creates sample buffers.

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
class AVSampleBufferGenerator
```

#### Overview

Each request for `CMSampleBuffer` creation is described in an `AVSampleBufferRequest` object. The [`CMSampleBuffer`](https://developer.apple.com/documentation/CoreMedia/CMSampleBuffer) opaque objects are returned synchronously. If requested, sample data may be loaded asynchronously (depending on file format support).

## Topics

### Creating sample buffer generators
- [init(asset: AVAsset, timebase: CMTimebase?)](avsamplebuffergenerator/init(asset:timebase:).md)
  Creates a new sample buffer generator.
### Creating a sample buffer
- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> sending CMSampleBuffer](avsamplebuffergenerator/makesamplebuffer(for:).md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeBatch() -> AVSampleBufferGeneratorBatch](avsamplebuffergenerator/makebatch.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](avsamplebuffergenerator/makesamplebuffer(for:addto:).md)
  Creates a sample buffer and attempts to defer I/O for its data.
- [func createSampleBuffer(for: AVSampleBufferRequest) -> CMSampleBuffer?](avsamplebuffergenerator/createsamplebuffer(for:).md)
  Creates a new sample buffer reference for the specified buffer request.
### Retrieving sample buffer data
- [class func notifyOfDataReady(for: CMSampleBuffer, completionHandler: (Bool, (any Error)?) -> Void)](avsamplebuffergenerator/notifyofdataready(for:completionhandler:).md)
  Notifies the sample buffer generator when data is ready for the sample buffer reference or an error has occurred.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Playing custom audio with your own player](../AVFAudio/playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [class AVSampleBufferRequest](avsamplebufferrequest.md)
  An object that describes a sample buffer creation request.
- [class AVSampleBufferGeneratorBatch](avsamplebuffergeneratorbatch.md)
  An object that generates sample buffers in a batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator)*