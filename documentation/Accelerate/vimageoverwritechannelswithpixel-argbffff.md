# vImageOverwriteChannelsWithPixel_ARGBFFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 5.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func vImageOverwriteChannelsWithPixel_ARGBFFFF(_ the_pixel: UnsafePointer<Float>!, _ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ copyMask: UInt8, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code overwrites channel `0` of the source pixels in `pixelBuffer` with channel `0` of the source pixel value:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [10, 20, 30, 40,
                  50, 60, 70, 80],
    size: .init(width: 1, height: 2))

let pixel: [Pixel_F] =  [101, 102, 103, 104]

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageOverwriteChannelsWithPixel_ARGBFFFF(pixel,
                                                 buf,
                                                 buf,
                                                 0x8,
                                                 vImage_Flags(kvImageNoFlags))
}

// Prints:
//      "[101.0, 20.0, 30.0, 40.0,
//        101.0, 60.0, 70.0, 80.0]"
print(pixelBuffer.array)
```

## Parameters

- `the_pixel`: The source pixel value that provides the new channel values.
- `src`: The source vImage buffer that provides the original pixel values.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `copyMask`: A bitmask that specifies the channel or channels that the function overwrites with the corresponding channel in the   parameter. The value   represents channel  , the value   represents channel  , the value   represents channel  , and the value   represents channel  .
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageOverwriteChannelsWithPixel_ARGB8888(UnsafePointer<UInt8>!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithpixel_argb8888(_:_:_:_:_:).md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.
- [func vImageOverwriteChannelsWithPixel_ARGB16U(UnsafePointer<UInt16>!, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithpixel_argb16u(_:_:_:_:_:).md)
  Overwrites the channels of an unsigned 16-bit-per-channel, 4-channel interleaved buffer with the specified channels of a pixel value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageoverwritechannelswithpixel_argbffff(_:_:_:_:_:))*