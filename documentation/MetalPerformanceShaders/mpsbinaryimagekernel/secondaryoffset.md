# secondaryOffset

**Framework**: Metal Performance Shaders  
**Kind**: property

The position of the destination clip rectangle origin relative to the secondary source buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var secondaryOffset: MPSOffset { get set }
```

#### Discussion

The offset is defined to be the position of the `origin` value of [`clipRect`](mpsbinaryimagekernel/cliprect.md), in source coordinates.

The default value is `{0, 0, 0}`, indicating that the top left corners of the clip rectangle and the secondary source image align.

## See Also

- [var primaryOffset: MPSOffset](mpsbinaryimagekernel/primaryoffset.md)
  The position of the destination clip rectangle origin relative to the primary source buffer.
- [var primaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/primaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the primary source image.
- [var secondaryEdgeMode: MPSImageEdgeMode](mpsbinaryimagekernel/secondaryedgemode.md)
  The edge mode to use when texture reads stray off the edge of the secondary source image.
- [var clipRect: MTLRegion](mpsbinaryimagekernel/cliprect.md)
  An optional clip rectangle to use when writing data. Only the pixels in the rectangle will be overwritten.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsbinaryimagekernel/secondaryoffset)*