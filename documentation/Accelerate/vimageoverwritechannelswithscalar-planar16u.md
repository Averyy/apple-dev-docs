# vImageOverwriteChannelsWithScalar_Planar16U(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Overwrites an unsigned 16-bit planar buffer with the specified scalar value in place.

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
func vImageOverwriteChannelsWithScalar_Planar16U(_ scalar: Pixel_16U, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

The following code fills `pixelBuffer` with `scalar`:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.Planar16U>(
    size: .init(width: 4, height: 1))

let scalar: Pixel_16U = 101

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageOverwriteChannelsWithScalar_Planar16U(scalar,
                                                    buf,
                                                    vImage_Flags(kvImageNoFlags))
}

// Prints "[101, 101, 101, 101]".
print(pixelBuffer.array)
```

## Parameters

- `scalar`: The scalar value that provides the new pixel values.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the  ,  , and   fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .

## See Also

- [func vImageOverwriteChannelsWithScalar_Planar8(Pixel_8, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar8(_:_:_:).md)
  Overwrites an 8-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16S(Pixel_16S, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar16s(_:_:_:).md)
  Overwrites a signed 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16F(Pixel_16F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planar16f(_:_:_:).md)
  Overwrites a floating-point 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_PlanarF(Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_planarf(_:_:_:).md)
  Overwrites a floating-point 32-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_ARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_argb8888(_:_:_:_:_:).md)
  Overwrites the selected channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.
- [func vImageOverwriteChannelsWithScalar_ARGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](vimageoverwritechannelswithscalar_argbffff(_:_:_:_:_:).md)
  Overwrites the selected channels of a 32-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageoverwritechannelswithscalar_planar16u(_:_:_:))*