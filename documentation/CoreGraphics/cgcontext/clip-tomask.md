# clip(to:mask:)

**Framework**: Core Graphics  
**Kind**: method

Maps a mask into the specified rectangle and intersects it with the current clipping area of the graphics context.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func clip(to rect: CGRect, mask: CGImage)
```

#### Discussion

If the `mask` parameter is an image mask, then Core Graphics clips in a manner identical to the behavior seen with the [`CGContextDrawImage`](cgcontextdrawimage.md) function —the mask indicates an area to be left unchanged when drawing. The source samples of the image mask determine which points of the clipping area are changed, acting as an “inverse alpha” value. If the value of a source sample in the image mask is `S`, then the corresponding point in the current clipping area is multiplied by an alpha value of (`1–S`). For example, if `S` is `1` then the point in the clipping area becomes transparent. If `S` is `0`, the point in the clipping area is unchanged.

If the `mask` parameter is an image, then `mask` acts like an alpha mask and is blended with the current clipping area. The source samples of mask determine which points of the clipping area are changed. If the value of the source sample in mask is `S`, then the corresponding point in the current clipping area is multiplied by an alpha of `S`. For example, if `S` is `0`, then the point in the clipping area becomes transparent. If `S` is `1`, the point in the clipping area is unchanged.

## Parameters

- `rect`: The rectangle to map the   parameter to.
- `mask`: An image or an image mask. If   is an image, then it must be in the DeviceGray color space, may not have an alpha component, and may not be masked by an image mask or masking color.

## See Also

- [func clip(using: CGPathFillRule)](cgcontext/clip(using:).md)
  Modifies the current clipping path.
- [func clip(to: CGRect)](cgcontext/clip(to:)-7cbwq.md)
  Sets the clipping path to the intersection of the current clipping path with the area defined by the specified rectangle.
- [func clip(to: [CGRect])](cgcontext/clip(to:)-2eg0.md)
  Sets the clipping path to the intersection of the current clipping path with the region defined by an array of rectangles.
- [var boundingBoxOfClipPath: CGRect](cgcontext/boundingboxofclippath.md)
  Returns the bounding box of a clipping path.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgcontext/clip(to:mask:))*