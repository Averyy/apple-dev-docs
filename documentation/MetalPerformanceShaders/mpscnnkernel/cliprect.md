# clipRect

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var clipRect: MTLRegion { get set }
```

```objc
@property (nonatomic, readwrite) MTLRegion clipRect;
```

#### Discussion

A region that indicates which part of the destination image to overwrite. If the clip rectangle does not lie completely within the destination image, the intersection between the clip rectangle and the destination image bounds is used instead.

The default value is [`MPSRectNoClip`](../mpsrectnoclip.md), indicating that the entire destination image will be overwritten.

The value of `clipRect.origin.z` is the index of the starting destination image in batch processing mode. The value of `clipRect.size.depth` is the number of images to process in batch processing mode.

## See Also

### Instance Properties
- [var offset: MPSOffset](./offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [struct MPSOffset](../mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [struct MTLRegion](../../Metal/mtlregion.md)
  The bounds for a subset of an instance’s elements.
- [var destinationFeatureChannelOffset: Int](./destinationfeaturechanneloffset.md)
  The number of channels in the destination image to skip before writing output data.
- [var edgeMode: MPSImageEdgeMode](./edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](../mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.
- [var kernelHeight: Int](./kernelheight.md)
- [var kernelWidth: Int](./kernelwidth.md)
- [var strideInPixelsX: Int](./strideinpixelsx.md)
- [var strideInPixelsY: Int](./strideinpixelsy.md)
- [var isBackwards: Bool](./isbackwards.md)
- [var padding: any MPSNNPadding](./padding.md)
- [protocol MPSNNPadding](../mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var destinationImageAllocator: any MPSImageAllocator](./destinationimageallocator.md)
- [protocol MPSImageAllocator](../mpsimageallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/cliprect)*