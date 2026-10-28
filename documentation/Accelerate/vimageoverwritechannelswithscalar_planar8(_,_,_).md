# vImageOverwriteChannelsWithScalar_Planar8(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Overwrites an 8-bit planar buffer with the specified scalar value in place.

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
func vImageOverwriteChannelsWithScalar_Planar8(_ scalar: Pixel_8, _ dest: UnsafePointer<vImage_Buffer>, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageOverwriteChannelsWithScalar_Planar8(Pixel_8 scalar, const vImage_Buffer *dest, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

The following code fills `pixelBuffer` with `scalar`:

**Swift**:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.Planar8>(
    size: .init(width: 4, height: 1))

let scalar: Pixel_8 = 101

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    _ = vImageOverwriteChannelsWithScalar_Planar8(scalar,
                                              buf,
                                              vImage_Flags(kvImageNoFlags))
}

// Prints "[101, 101, 101, 101]".
print(pixelBuffer.array)
```

**Objective-C**:

```objc
uint8_t data[4] = {0, 0, 0, 0};

vImage_Buffer buf = {
    .data = data,
    .width = 4,
    .height = 1,
    .rowBytes = 4
};

Pixel_8 scalar = 101;

vImageOverwriteChannelsWithScalar_Planar8(scalar,
                                          &buf,
                                          kvImageNoFlags);

// Prints "[101, 101, 101, 101]".
printf("[%d, %d, %d, %d]\n",
       data[0], data[1], data[2], data[3]);
```

## Parameters

- `scalar`: The scalar value that provides the new pixel values.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Overwriting with scalar values
- [func vImageOverwriteChannelsWithScalar_Planar16U(Pixel_16U, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_planar16u%28_,_,_%29.md)
  Overwrites an unsigned 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16S(Pixel_16S, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_planar16s%28_,_,_%29.md)
  Overwrites a signed 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_Planar16F(Pixel_16F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_planar16f%28_,_,_%29.md)
  Overwrites a floating-point 16-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_PlanarF(Pixel_F, UnsafePointer<vImage_Buffer>, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_planarf%28_,_,_%29.md)
  Overwrites a floating-point 32-bit planar buffer with the specified scalar value in place.
- [func vImageOverwriteChannelsWithScalar_ARGB8888(Pixel_8, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_argb8888%28_,_,_,_,_%29.md)
  Overwrites the selected channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.
- [func vImageOverwriteChannelsWithScalar_ARGBFFFF(Pixel_F, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](./vimageoverwritechannelswithscalar_argbffff%28_,_,_,_,_%29.md)
  Overwrites the selected channels of a 32-bit-per-channel, 4-channel interleaved buffer with the specified scalar value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageoverwritechannelswithscalar_planar8(_:_:_:))*