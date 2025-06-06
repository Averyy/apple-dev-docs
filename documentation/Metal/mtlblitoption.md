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

### Depth and Stencil Buffer Options
- [static var depthFromDepthStencil: MTLBlitOption](mtlblitoption/depthfromdepthstencil.md)
  A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.
- [static var stencilFromDepthStencil: MTLBlitOption](mtlblitoption/stencilfromdepthstencil.md)
  A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.
### Texture Compression Options
- [static var rowLinearPVRTC: MTLBlitOption](mtlblitoption/rowlinearpvrtc.md)
  A blit option that copies PVRTC data between a texture and a buffer.
### Clearing Options
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
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [protocol MTLBlitCommandEncoder](mtlblitcommandencoder.md)
  An interface you can use to encode GPU commands that copy and modify the underlying memory of various Metal resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption)*