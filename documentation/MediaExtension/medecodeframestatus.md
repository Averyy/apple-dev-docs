# MEDecodeFrameStatus

**Framework**: MediaExtension  
**Kind**: struct

A type that represents a non-error status related to a frame decode operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MEDecodeFrameStatus
```

## Topics

### Creating a status
- [init(rawValue: UInt)](medecodeframestatus/init(rawvalue:).md)
  Creates a new frame decode operation status with the raw value that you specify.
### Inspecting a status
- [static var frameDropped: MEDecodeFrameStatus](medecodeframestatus/framedropped.md)
  A frame decode operation status that indicates the system dropped the output of the frame for a reason other than an error.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func canAccept(CMFormatDescription) -> Bool](mevideodecoder/canaccept(_:).md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [func decodeFrame(from: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)](mevideodecoder/decodeframe(from:options:completionhandler:).md)
  Requests the extension to decode a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframestatus)*