# depthFromDepthStencil

**Framework**: Metal  
**Kind**: property

A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static var depthFromDepthStencil: MTLBlitOption { get }
```

#### Discussion

You can pass this option to some methods that copy data between a buffer and a texture, including the following:

- [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](mtlblitcommandencoder/copy(from:sourceoffset:sourcebytesperrow:sourcebytesperimage:sourcesize:to:destinationslice:destinationlevel:destinationorigin:options:).md)
- [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](mtlblitcommandencoder/copy(from:sourceslice:sourcelevel:sourceorigin:sourcesize:to:destinationoffset:destinationbytesperrow:destinationbytesperimage:options:).md)

## See Also

- [static var stencilFromDepthStencil: MTLBlitOption](mtlblitoption/stencilfromdepthstencil.md)
  A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption/depthfromdepthstencil)*