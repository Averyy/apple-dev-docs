# vImageGetPerspectiveWarp(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a projective-transformation structure that defines the mapping between a source quadrilateral and a destination quadrilateral.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func vImageGetPerspectiveWarp(_ srcPoints: UnsafePointer<(Float, Float)>, _ destPoints: UnsafePointer<(Float, Float)>, _ transform: UnsafeMutablePointer<vImage_PerpsectiveTransform>, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

## Parameters

- `srcPoints`: The four source points.
- `destPoints`: The four destination points.
- `transform`: On output, a   structure that describes the transformation from the source points to the destination points.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Transforming an image in three dimensions](transforming-an-image-in-three-dimensions.md)
  Create and use a projective transformation to apply a perspective warp to an image.
- [struct vImage_PerpsectiveTransform](vimage_perpsectivetransform.md)
  A projective-transformation matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagegetperspectivewarp(_:_:_:_:))*