# padding

**Framework**: Metal Performance Shaders  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var padding: any MPSNNPadding { get set }
```

```objc
@property (nonatomic, retain, readwrite, nonnull) id<MPSNNPadding> padding;
```

## See Also

### Instance Properties
- [var offset: MPSOffset](./offset.md)
  The position of the destination image’s clip rectangle origin, relative to the source image.
- [struct MPSOffset](../mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](./cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the clip rectangle will be overwritten.
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
- [protocol MPSNNPadding](../mpsnnpadding.md)
  The protocol that provides a description of how kernels should pad images.
- [var destinationImageAllocator: any MPSImageAllocator](./destinationimageallocator.md)
- [protocol MPSImageAllocator](../mpsimageallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnkernel/padding)*