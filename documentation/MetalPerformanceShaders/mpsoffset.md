# MPSOffset

**Framework**: Metal Performance Shaders  
**Kind**: struct

A signed coordinate with x, y, and z components.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MPSOffset
```

## Topics

### Fields
- [var x: Int](mpsoffset/x.md)
  The horizontal component of the offset, in pixels.
- [var y: Int](mpsoffset/y.md)
  The vertical component of the offset, in pixels.
- [var z: Int](mpsoffset/z.md)
  The depth component of the offset, in pixels.
### Initializers
- [init()](mpsoffset/init.md)
- [init(x: Int, y: Int, z: Int)](mpsoffset/init(x:y:z:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var offset: MPSOffset](mpscnnkernel/offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [var clipRect: MTLRegion](mpscnnkernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
- [struct MTLRegion](../Metal/MTLRegion.md)
  The bounds for a subset of an instance’s elements.
- [var destinationFeatureChannelOffset: Int](mpscnnkernel/destinationfeaturechanneloffset.md)
  The number of channels in the destination image to skip before writing output data.
- [var edgeMode: MPSImageEdgeMode](mpscnnkernel/edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.
- [var kernelHeight: Int](mpscnnkernel/kernelheight.md)
- [var kernelWidth: Int](mpscnnkernel/kernelwidth.md)
- [var strideInPixelsX: Int](mpscnnkernel/strideinpixelsx.md)
- [var strideInPixelsY: Int](mpscnnkernel/strideinpixelsy.md)
- [var isBackwards: Bool](mpscnnkernel/isbackwards.md)
- [var padding: any MPSNNPadding](mpscnnkernel/padding.md)
- [protocol MPSNNPadding](mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var destinationImageAllocator: any MPSImageAllocator](mpscnnkernel/destinationimageallocator.md)
- [protocol MPSImageAllocator](mpsimageallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsoffset)*