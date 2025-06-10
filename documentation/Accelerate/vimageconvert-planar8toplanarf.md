# vImageConvert_Planar8toPlanarF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Converts an 8-bit planar buffer to a floating-point 32-bit planar buffer.

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
func vImageConvert_Planar8toPlanarF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ maxFloat: Pixel_F, _ minFloat: Pixel_F, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The function uses the following calculation to perform the conversion:

```objc
 float result = (maxFloat - minFloat) * (float) srcPixel / 255.0  + minFloat
```

The two buffers must have the same number of rows and the same number of columns.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `maxFloat`: The maximum pixel value for the destination image.
- `minFloat`: The minimum pixel value for the destination image.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_8to16Q12(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_8to16q12(_:_:_:).md)
  Converts an 8-bit planar buffer to a fixed-point 16-bit planar buffer.
- [func vImageConvert_Planar8toPlanar16F(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_planar8toplanar16f(_:_:_:).md)
  Converts an 8-bit planar buffer to a floating-point 16-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planar8toplanarf(_:_:_:_:_:))*