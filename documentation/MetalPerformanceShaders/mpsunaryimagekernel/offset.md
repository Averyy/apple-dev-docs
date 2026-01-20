# offset

**Framework**: Metal Performance Shaders  
**Kind**: property

The position of the destination clip rectangle origin relative to the source buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var offset: MPSOffset { get set }
```

#### Discussion

The offset is defined to be the position of the `origin` value of [`clipRect`](mpsunaryimagekernel/cliprect.md), in source coordinates.

The default value is `{0, 0, 0}`, indicating that the top left corners of the clip rectangle and the source image align.

## See Also

- [struct MPSOffset](mpsoffset.md)
  A signed coordinate with x, y, and z components.
- [var clipRect: MTLRegion](mpsunaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.
- [struct MPSRegion](mpsregion.md)
  A region of an image.
- [var edgeMode: MPSImageEdgeMode](mpsunaryimagekernel/edgemode.md)
  The edge mode to use when texture reads stray off the edge of an image.
- [enum MPSImageEdgeMode](mpsimageedgemode.md)
  The options used to control the edge behavior of an image filter when it reads outside the bounds of a source texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsunaryimagekernel/offset)*