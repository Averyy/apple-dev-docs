# CMIOExtensionStream.DiscontinuityFlags

**Framework**: Core Media I/O  
**Kind**: struct  
**Role**: Structure

Constants that specify the types of discontinuities that can occur in a media stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
struct DiscontinuityFlags
```

```c
enum CMIOExtensionStreamDiscontinuityFlags : uint32_t;
```

## Topics

### Discontinuity Flags
- [static var unknown: CMIOExtensionStream.DiscontinuityFlags](./discontinuityflags/unknown.md)
  A flag that indicates a stream discontinuity due to an unknown reason.
- [static var time: CMIOExtensionStream.DiscontinuityFlags](./discontinuityflags/time.md)
  A flag that indicates a time discontinuity in the stream.
- [static var sampleDropped: CMIOExtensionStream.DiscontinuityFlags](./discontinuityflags/sampledropped.md)
  A flag that indicates a discontinuity in the stream due to a dropped frame.
### Initializers
- [init(rawValue: UInt32)](./discontinuityflags/init%28rawvalue%29.md)
  Creates a flag with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Processing Data
- [func consumeSampleBuffer(from: CMIOExtensionClient, completionHandler: (CMSampleBuffer?, UInt64, CMIOExtensionStream.DiscontinuityFlags, Bool, (any Error)?) -> Void)](./consumesamplebuffer%28from,completionhandler%29.md)
  Consumes a sample buffer from a client.
- [func send(CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)](./send%28_,discontinuity,hosttimeinnanoseconds%29.md)
  Sends a media sample to stream client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/discontinuityflags)*