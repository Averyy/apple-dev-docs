# vImageConvert_ARGB1555toARGB8888(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an ARGB1555 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_ARGB1555toARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The ARGB1555 format has 16-bit pixels with 1 bit for alpha and 5 bits each for red, green, and blue. The function uses the following calculation to perform the conversion:

```objc
 destA->data[x] =  1bitAlphaChannel * 255;
 destR->data[x] = (5bitRedChannel   * 255 + 15) / 31;
 destG->data[x] = (5bitGreenChannel * 255 + 15) / 31;
 destB->data[x] = (5bitBlueChannel  * 255 + 15) / 31;
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_RGBA5551toRGBA8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba5551torgba8888(_:_:_:).md)
  Converts an RGB5651 4-channel interleaved buffer to an 8-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb1555toargb8888(_:_:_:))*