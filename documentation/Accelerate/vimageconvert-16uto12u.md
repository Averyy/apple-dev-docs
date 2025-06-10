# vImageConvert_16UTo12U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an unsigned 16-bit planar buffer to an unsigned 12-bit planar buffer.

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
func vImageConvert_16UTo12U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```c
 uint16_t *srcRow = srcData;
 uint8_t *destRow = destData;
 
 // Two 16-bit in 4-bytes.
 t0 = srcRow[0];
 t1 = srcRow[1];
 srcRow += 2;
 
 t0 = (t0 * 4095 + 32767 + (t0 >> 4)) >> 16;
 t1 = (t1 * 4095 + 32767 + (t1 >> 4)) >> 16;
 
 t0 <<= 12;
 t0 |= t1;
 
 // Two 12-bit in 3-bytes.
 destRow[0] = t0 >> 16;
 destRow[1] = t0 >> 8;
 destRow[2] = t0;
 destRow += 3;
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_16UToPlanar8(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_16utoplanar8(_:_:_:).md)
  Converts an unsigned 16-bit planar buffer to an 8-bit planar buffer.
- [func vImageConvert_Planar16UtoPlanar8_dithered(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int32, vImage_Flags) -> vImage_Error](vimageconvert_planar16utoplanar8_dithered(_:_:_:_:).md)
  Converts an unsigned 16-bit planar buffer to an 8-bit planar buffer using the specified dithering algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_16uto12u(_:_:_:))*