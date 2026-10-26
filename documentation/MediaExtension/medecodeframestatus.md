# MEDecodeFrameStatus

**Framework**: MediaExtension  
**Kind**: struct  
**Role**: Structure

A type that represents a non-error status related to a frame decode operation.

**Availability**:
- macOS 14.0+

## Declaration

```swift
struct MEDecodeFrameStatus
```

```c
enum MEDecodeFrameStatus : NSUInteger;
```

## Topics

### Creating a status
- [init(rawValue: UInt)](./medecodeframestatus/init%28rawvalue%29.md)
  Creates a new frame decode operation status with the raw value that you specify.
### Inspecting a status
- [static var frameDropped: MEDecodeFrameStatus](./medecodeframestatus/framedropped.md)
  A frame decode operation status that indicates the system dropped the output of the frame for a reason other than an error.
- [MEDecodeFrameNoStatus](./medecodeframestatus/medecodeframenostatus.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Decoding frames
- [func canAccept(CMFormatDescription) -> Bool](./mevideodecoder/canaccept%28_%29.md)
  Asks the extension whether the decoder can decode frames with the format description that you specify.
- [func decodeFrame(from: CMSampleBuffer, options: MEDecodeFrameOptions, completionHandler: (CVImageBuffer?, MEDecodeFrameStatus, (any Error)?) -> Void)](./mevideodecoder/decodeframe%28from,options,completionhandler%29.md)
  Requests the extension to decode a video frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaextension/medecodeframestatus)*