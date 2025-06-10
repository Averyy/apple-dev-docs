# vImageConvert_ARGB1555toPlanar8(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deinterleaves an ARGB1555 4-channel interleaved buffer into four 8-bit planar buffers.

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
func vImageConvert_ARGB1555toPlanar8(_ src: UnsafePointer<vImage_Buffer>, _ destA: UnsafePointer<vImage_Buffer>, _ destR: UnsafePointer<vImage_Buffer>, _ destG: UnsafePointer<vImage_Buffer>, _ destB: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
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
- `destA`: A pointer to the alpha destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the alpha destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destR`: A pointer to the red destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the red destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destG`: A pointer to the green destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the green destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `destB`: A pointer to the blue destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the blue destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb1555toplanar8(_:_:_:_:_:_:))*