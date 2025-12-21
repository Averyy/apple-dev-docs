# MTLBlitOption

**Framework**: Metal  
**Kind**: struct

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

## Topics

### Depth and stencil buffer options
- [static var depthFromDepthStencil: MTLBlitOption](mtlblitoption/depthfromdepthstencil.md)
  A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.
- [static var stencilFromDepthStencil: MTLBlitOption](mtlblitoption/stencilfromdepthstencil.md)
  A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.
### Texture compression options
- [static var rowLinearPVRTC: MTLBlitOption](mtlblitoption/rowlinearpvrtc.md)
  A blit option that copies PVRTC data between a texture and a buffer.
### Swift support
- [init(rawValue: UInt)](mtlblitoption/init(rawvalue:).md)
  Creates a blit option from a raw value.

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

- [protocol MTLBlitCommandEncoder](mtlblitcommandencoder.md)
  Encodes commands that copy and modify resources for a single blit pass.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption)*