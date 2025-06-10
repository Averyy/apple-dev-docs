# vImageTableLookUp_ARGB8888(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Uses a lookup table to transform an interleaved, four-channel 8-bit planar image to an interleaved, four-channel 8-bit planar image.

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
func vImageTableLookUp_ARGB8888(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ alphaTable: UnsafePointer<Pixel_8>!, _ redTable: UnsafePointer<Pixel_8>!, _ greenTable: UnsafePointer<Pixel_8>!, _ blueTable: UnsafePointer<Pixel_8>!, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `alphaTable`: A lookup table for the alpha channel that contains 256   values. Pass   to specify that the function copies the alpha channel unchanged to the destination buffer.
- `redTable`: A lookup table for the red channel that contains 256   values. Pass   to specify that the function copies the alpha channel unchanged to the destination buffer.
- `greenTable`: A lookup table for the green channel that contains 256   values. Pass   to specify that the function copies the alpha channel unchanged to the destination buffer.
- `blueTable`: A lookup table for the blue channel that contains 256   values. Pass   to specify that the function copies the alpha channel unchanged to the destination buffer.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagetablelookup_argb8888(_:_:_:_:_:_:_:))*