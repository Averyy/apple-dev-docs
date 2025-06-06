# CMIOExtensionStream.DiscontinuityFlags

**Framework**: Core Media I/O  
**Kind**: struct

Constants that specify the types of discontinuities that can occur in a media stream.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
struct DiscontinuityFlags
```

## Topics

### Discontinuity Flags
- [static var unknown: CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags/unknown.md)
  A flag that indicates a stream discontinuity due to an unknown reason.
- [static var time: CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags/time.md)
  A flag that indicates a time discontinuity in the stream.
- [static var sampleDropped: CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags/sampledropped.md)
  A flag that indicates a discontinuity in the stream due to a dropped frame.
### Initializers
- [init(rawValue: UInt32)](cmioextensionstream/discontinuityflags/init(rawvalue:).md)
  Creates a flag with an integer value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func consumeSampleBuffer(from: CMIOExtensionClient, completionHandler: (CMSampleBuffer?, UInt64, CMIOExtensionStream.DiscontinuityFlags, Bool, (any Error)?) -> Void)](cmioextensionstream/consumesamplebuffer(from:completionhandler:).md)
  Consumes a sample buffer from a client.
- [func send(CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)](cmioextensionstream/send(_:discontinuity:hosttimeinnanoseconds:).md)
  Sends a media sample to stream client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/discontinuityflags)*