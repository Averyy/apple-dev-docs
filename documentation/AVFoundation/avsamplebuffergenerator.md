# AVSampleBufferGenerator

**Framework**: AVFoundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface AVSampleBufferGenerator : NSObject
```

#### Overview

Each request for `CMSampleBuffer` creation is described in an `AVSampleBufferRequest` object. The [`CMSampleBuffer`](../CoreMedia/cmsamplebuffer.md) opaque objects are returned synchronously. If requested, sample data may be loaded asynchronously (depending on file format support).

## Topics

### Creating sample buffer generators
- [init(asset: AVAsset, timebase: CMTimebase?)](./avsamplebuffergenerator/init%28asset,timebase%29.md)
  Creates a new sample buffer generator.
### Creating a sample buffer
- [func makeSampleBuffer(for: AVSampleBufferRequest) throws -> sending CMSampleBuffer](./avsamplebuffergenerator/makesamplebuffer%28for%29.md)
  Creates a sample buffer, and attempts to load its data asynchronously if requested.
- [func makeBatch() -> AVSampleBufferGeneratorBatch](./avsamplebuffergenerator/makebatch%28%29.md)
  Creates a batch object to handle generating multiple sample buffers.
- [func makeSampleBuffer(for: AVSampleBufferRequest, addTo: AVSampleBufferGeneratorBatch) throws -> CMSampleBuffer](./avsamplebuffergenerator/makesamplebuffer%28for,addto%29.md)
  Creates a sample buffer and attempts to defer I/O for its data.
- [func createSampleBuffer(for: AVSampleBufferRequest) -> CMSampleBuffer?](./avsamplebuffergenerator/createsamplebuffer%28for%29.md)
  Creates a new sample buffer reference for the specified buffer request.
### Retrieving sample buffer data
- [class func notifyOfDataReady(for: CMSampleBuffer, completionHandler: (Bool, (any Error)?) -> Void)](./avsamplebuffergenerator/notifyofdataready%28for,completionhandler%29.md)
  Notifies the sample buffer generator when data is ready for the sample buffer reference or an error has occurred.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sample buffer generation
- [Playing custom audio with your own player](../AVFAudio/playing-custom-audio-with-your-own-player.md)
  Construct an audio player to play your custom audio data, and optionally take advantage of the advanced features of AirPlay 2.
- [class AVSampleBufferRequest](./avsamplebufferrequest.md)
  An object that describes a sample buffer creation request.
- [class AVSampleBufferGeneratorBatch](./avsamplebuffergeneratorbatch.md)
  An object that generates sample buffers in a batch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsamplebuffergenerator)*