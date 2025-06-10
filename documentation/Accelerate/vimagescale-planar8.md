# vImageScale_Planar8(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Scales an 8-bit planar image to fit a destination buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.3+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageScale_Planar8(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ flags: vImage_Flags) -> vImage_Error
```

## Mentions

- [Optimizing image-processing performance](optimizing-image-processing-performance.md)

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes described in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The relative dimensions of the source image and the destination buffer determine the scaling factors. The function supports nonuniform scaling — that is, the horizontal and vertical ratios can be different.

To avoid artifacts in high-frequency regions of the image, supply image data that’s nonpremultiplied or that has a constant alpha over the entire image.

This function doesn’t work in place — that is, the source and destination buffers must point to different memory.

## Parameters

- `src`: A pointer to a vImage buffer structure that contains the source image.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `flags`: This function ignores the   flag.

## See Also

- [Applying geometric transforms to images](applying-geometric-transforms-to-images.md)
  Reflect, shear, rotate, and scale image buffers using vImage.
- [func vImageScale_Planar16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16u(_:_:_:_:).md)
  Scales an unsigned 16-bit planar image to fit a destination buffer.
- [func vImageScale_Planar16S(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16s(_:_:_:_:).md)
  Scales a signed 16-bit planar image to fit a destination buffer.
- [func vImageScale_Planar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planar16f(_:_:_:_:).md)
  Scales a floating-point 16-bit planar image to fit a destination buffer.
- [func vImageScale_PlanarF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, vImage_Flags) -> vImage_Error](vimagescale_planarf(_:_:_:_:).md)
  Scales a 32-bit planar image to fit a destination buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagescale_planar8(_:_:_:_:))*