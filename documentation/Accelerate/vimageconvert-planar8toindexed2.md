# vImageConvert_Planar8toIndexed2(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit planar buffer to an indexed 2-bit planar buffer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 7.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_Planar8toIndexed2(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ tempBuffer: UnsafeMutableRawPointer!, _ colors: UnsafeMutablePointer<Pixel_8>, _ dither: Int32, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function supports the following dithering algorithms:

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `tempBuffer`: A pointer to a temporary buffer. If you pass  , the function allocates the buffer and then deallocates it before returning. Alternatively, you can allocate the buffer yourself, in which case you’re responsible for deallocating it when you no longer need it.
- `colors`: The lookup table. To specify that the function computes the color table, pass a table filled with zeros.
- `dither`: The dithering algorithm.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [Improving the quality of quantized images with dithering](improving-the-quality-of-quantized-images-with-dithering.md)
  Apply dithering to simulate colors that are unavailable in reduced bit depths.
- [func vImageConvert_Planar8toPlanar1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar1(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a 1-bit planar buffer.
- [func vImageConvert_Planar8toPlanar2(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar2(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a 2-bit planar buffer.
- [func vImageConvert_Planar8toPlanar4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar4(_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to a 4-bit planar buffer.
- [func vImageConvert_Planar8toIndexed1(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toindexed1(_:_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to an indexed 1-bit planar buffer.
- [func vImageConvert_Planar8toIndexed4(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, UnsafeMutablePointer<Pixel_8>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar8toindexed4(_:_:_:_:_:_:).md)
  Converts an 8-bit planar buffer to an indexed 4-bit planar buffer.
- [func vImageConvert_Planar8To16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8to16u(_:_:_:).md)
  Converts an 8-bit planar buffer to an unsigned 16-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8toindexed2(_:_:_:_:_:_:))*