# vImageConvert_ARGB8888ToARGB16U(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit-per-channel, 4-channel interleaved buffer to an unsigned 16-bit-per-channel, 4-channel buffer with permutation.

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
func vImageConvert_ARGB8888ToARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ permuteMap: UnsafePointer<UInt8>, _ copyMask: UInt8, _ backgroundColor: UnsafePointer<UInt16>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
 Pixel_8888 *srcPixel;
 Pixel_16U *destPixel;
 uint8_t result8;
 uint16_t result[4];
 uint8_t mask = 0x8;
 
 for( int i = 0; i < 4; i++ )
 {
     result8 = srcPixel[ permuteMap[i] ];
     result[i] = (result8 * 65535U + 127U) / 255U;
     if( mask & copyMask )
         result[i] = backgroundColor[i];
     mask = mask >> 1;
 }
 srcPixel += 4;
 
 destPixel[0] = result[0];
 destPixel[1] = result[1];
 destPixel[2] = result[2];
 destPixel[3] = result[3];
 destPixel += 4;
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `copyMask`: A bitmask that specifies the channel from the background color that the function copies to the destination channel at the corresponding index. The   bit corresponds to the alpha channel, the   bit corresponds to the red channel, the   corresponds to the green channel, and the   bit corresponds to the green channel.
- `backgroundColor`: A 16-bit-per-channel, 4-channel pixel value that replaces the destination pixels based on the copy mask.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_RGB888toRGB565_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgb888torgb565_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 3-channel interleaved buffer to an RGB565 3-channel interleaved buffer using the specified dithering algorithm.
- [func vImageConvert_ARGB8888toARGB1555(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toargb1555(_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an ARGB1555 4-channel interleaved buffer.
- [func vImageConvert_ARGB8888toARGB1555_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_argb8888toargb1555_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an ARGB1555 4-channel interleaved buffer usng the specified dithering algorithm.
- [func vImageConvert_RGBA8888toRGBA5551(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgba5551(_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an RGBA5551 4-channel interleaved buffer.
- [func vImageConvert_RGBA8888toRGBA5551_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafeMutableRawPointer!, Int32, vImage_Flags) -> vImage_Error](vimageconvert_rgba8888torgba5551_dithered(_:_:_:_:_:).md)
  Converts an 8-bit-per-channel, 4-channel interleaved buffer to an RGBA5551 4-channel interleaved buffer usng the specified dithering algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb8888toargb16u(_:_:_:_:_:_:))*