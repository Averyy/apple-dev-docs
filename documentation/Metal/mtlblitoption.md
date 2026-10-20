# MTLBlitOption

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The options that enable behavior for some blit operations.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLBlitOption
```

```c
enum MTLBlitOption : NSUInteger;
```

## Topics

### Depth and stencil buffer options
- [static var depthFromDepthStencil: MTLBlitOption](./mtlblitoption/depthfromdepthstencil.md)
  A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.
- [static var stencilFromDepthStencil: MTLBlitOption](./mtlblitoption/stencilfromdepthstencil.md)
  A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.
### Texture compression options
- [static var rowLinearPVRTC: MTLBlitOption](./mtlblitoption/rowlinearpvrtc.md)
  A blit option that copies PVRTC data between a texture and a buffer.
### Swift support
- [init(rawValue: UInt)](./mtlblitoption/init%28rawvalue%29.md)
  Creates a blit option from a raw value.

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

### Encoding a blit pass
- [protocol MTLBlitCommandEncoder](./mtlblitcommandencoder.md)
  Encodes commands that copy and modify resources for a single blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption)*