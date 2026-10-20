# depthFromDepthStencil

**Framework**: Metal  
**Kind**: property  
**Role**: Type Property

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

```c
MTLBlitOptionDepthFromDepthStencil
```

#### Discussion

You can pass this option to some methods that copy data between a buffer and a texture, including the following:

- [`copy(from:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:to:destinationSlice:destinationLevel:destinationOrigin:options:)`](../mtlblitcommandencoder/copy%28from,sourceoffset,sourcebytesperrow,sourcebytesperimage,sourcesize,to,destinationslice,destinationlevel,destinationorigin,options%29.md)
- [`copy(from:sourceSlice:sourceLevel:sourceOrigin:sourceSize:to:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:)`](../mtlblitcommandencoder/copy%28from,sourceslice,sourcelevel,sourceorigin,sourcesize,to,destinationoffset,destinationbytesperrow,destinationbytesperimage,options%29.md)

## See Also

### Depth and stencil buffer options
- [static var stencilFromDepthStencil: MTLBlitOption](./stencilfromdepthstencil.md)
  A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlblitoption/depthfromdepthstencil)*