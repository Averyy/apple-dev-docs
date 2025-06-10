# vImageErode_PlanarF(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Erodes a 32-bit planar buffer.

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
func vImageErode_PlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ srcOffsetToROI_X: vImagePixelCount, _ srcOffsetToROI_Y: vImagePixelCount, _ kernel: UnsafePointer<Float>, _ kernel_height: vImagePixelCount, _ kernel_width: vImagePixelCount, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Use the erode operation to enlarge dark structural elements in an image. In the case where the kernel contains all zeros, use the corresponding minimize function instead.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `srcOffsetToROI_X`: The horizontal offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `srcOffsetToROI_Y`: The vertical offset, in pixels, to the upper-left pixel of the region of interest within the source image.
- `kernel`: The kernel data that contains   elements.
- `kernel_height`: The height of the kernel in pixels. This value must be odd.
- `kernel_width`: The width of the kernel in pixels. This value must be odd.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Adding a bokeh effect to images](adding-a-bokeh-effect-to-images.md)
  Simulate a bokeh effect by applying dilation.
- [func vImageErode_Planar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimageerode_planar8(_:_:_:_:_:_:_:_:).md)
  Erodes an 8-bit planar buffer.
- [func vImageErode_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<UInt8>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimageerode_argb8888(_:_:_:_:_:_:_:_:).md)
  Erodes an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImageErode_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImagePixelCount, vImagePixelCount, UnsafePointer<Float>, vImagePixelCount, vImagePixelCount, vImage_Flags) -> vImage_Error](vimageerode_argbffff(_:_:_:_:_:_:_:_:).md)
  Erodes a 32-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageerode_planarf(_:_:_:_:_:_:_:_:))*