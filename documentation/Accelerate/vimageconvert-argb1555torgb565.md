# vImageConvert_ARGB1555toRGB565(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Removes the alpha channel from an ARGB1555 buffer to produce an RGB565 result.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 8.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageConvert_ARGB1555toRGB565(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This function copies the red, green, and blue source channels to the destination buffer.

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageConvert_RGBA5551toRGB565(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageconvert_rgba5551torgb565(_:_:_:).md)
  Removes the alpha channel from an RGBA5551 buffer to produce an RGB565 result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_argb1555torgb565(_:_:_:))*