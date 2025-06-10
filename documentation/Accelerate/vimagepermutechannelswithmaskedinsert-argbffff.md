# vImagePermuteChannelsWithMaskedInsert_ARGBFFFF(_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Permutes and overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer.

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
func vImagePermuteChannelsWithMaskedInsert_ARGBFFFF(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ permuteMap: UnsafePointer<UInt8>, _ copyMask: UInt8, _ backgroundColor: UnsafePointer<Float>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

This fused operation provides the same functionality as [`vImagePermuteChannels_ARGBFFFF(_:_:_:_:)`](vimagepermutechannels_argbffff(_:_:_:_:).md) followed by [`vImageOverwriteChannelsWithScalar_ARGBFFFF(_:_:_:_:_:)`](vimageoverwritechannelswithscalar_argbffff(_:_:_:_:_:).md) but offers higher performance than calling the two functions separately.

The following code reverses the channel ordering of a pixel buffer and overwrites channel `0` of the destination with element `0` of the background color:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [10, 20, 30, 40],
    size: .init(width: 1, height: 1))

let backgroundColor: [Pixel_F] = [101, 102, 103, 104]

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImagePermuteChannelsWithMaskedInsert_ARGBFFFF(buf,
                                                      buf,
                                                      [3, 2, 1, 0],
                                                      0x8,
                                                      backgroundColor,
                                                      vImage_Flags(kvImageNoFlags))
}

// Prints "[101, 30, 20, 10]".
print(pixelBuffer.array)
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `permuteMap`: An array of four 8-bit integers with the values  ,  ,  , and 3, in some order. Each value specifies the channel from the source image that the function copies to the destination channel at the corresponding index.
- `copyMask`: A bitmask that specifies the channel or channels that the function overwrites with the corresponding channel in the   parameter. The value   represents channel  , the value   represents channel  , the value   represents channel  , and the value   represents channel  .
- `backgroundColor`: The 32-bit-per-channel ARGB value that the function writes to the destination based on the   value.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImagePermuteChannelsWithMaskedInsert_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt8>, vImage_Flags) -> vImage_Error](vimagepermutechannelswithmaskedinsert_argb8888(_:_:_:_:_:_:).md)
  Permutes and overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer.
- [func vImagePermuteChannelsWithMaskedInsert_ARGB16U(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<UInt8>, UInt8, UnsafePointer<UInt16>, vImage_Flags) -> vImage_Error](vimagepermutechannelswithmaskedinsert_argb16u(_:_:_:_:_:_:).md)
  Permutes and overwrites the channels of an unsigned 16-bit-per-channel, 4-channel interleaved buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimagepermutechannelswithmaskedinsert_argbffff(_:_:_:_:_:_:))*