# edgeMode

**Framework**: Metal Performance Shaders  
**Kind**: property

The edge mode to use when texture reads stray off the edge of an image.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var edgeMode: MPSImageEdgeMode { get set }
```

#### Discussion

Most [`MPSKernel`](mpskernel.md) objects can read off the edge of the source image. This can happen because of a negative offset property, because the  value of `offset + clipRect.size` is larger than the source image or because the filter looks at neighboring pixels, such as a convolution filter.

The default value is [`MPSImageEdgeMode.zero`](mpsimageedgemode/zero.md).

> **Note**:  For an [`MPSCNNPoolingAverage`](mpscnnpoolingaverage.md) object, specifying a [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md) edge mode is interpreted as a “shrink-to-edge” operation, which shrinks the effective filtering window to remain within the source image borders.

## See Also

- [var offset: MPSOffset](mpscnnkernel/offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpscnnkernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
- [struct MTLRegion](../Metal/MTLRegion.md)
  The bounds for a subset of an instance’s elements.
- [var destinationFeatureChannelOffset: Int](mpscnnkernel/destinationfeaturechanneloffset.md)
  The number of channels in the destination image to skip before writing output data.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/edgemode)*