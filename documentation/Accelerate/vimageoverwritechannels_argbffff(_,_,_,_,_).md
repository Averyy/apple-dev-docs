# vImageOverwriteChannels_ARGBFFFF(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the corresponding pixels of a planar buffer.

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
func vImageOverwriteChannels_ARGBFFFF(_ newSrc: UnsafePointer<vImage_Buffer>, _ origSrc: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ copyMask: UInt8, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageOverwriteChannels_ARGBFFFF(const vImage_Buffer *newSrc, const vImage_Buffer *origSrc, const vImage_Buffer *dest, uint8_t copyMask, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

The following code overwrites channel `0` of the source pixels in `pixelBuffer` with the corresponding source pixels from `newSource`:

**Swift**:

```swift
let pixelBuffer = vImage.PixelBuffer<vImage.InterleavedFx4>(
    pixelValues: [10, 20, 30, 40,
                  50, 60, 70, 80],
    size: .init(width: 1, height: 2))

let newSource = vImage.PixelBuffer<vImage.PlanarF>(
    pixelValues: [101,
                  105],
    size: .init(width: 1, height: 2))

pixelBuffer.withUnsafePointerToVImageBuffer { buf in
    newSource.withUnsafePointerToVImageBuffer { new in
        _ = vImageOverwriteChannels_ARGBFFFF(new,
                                             buf,
                                             buf,
                                             0x8,
                                             vImage_Flags(kvImageNoFlags))
    }
}

// Prints:
//      "[101.0, 20.0, 30.0, 40.0,
//        105.0, 60.0, 70.0, 80.0]".
print(pixelBuffer.array)
```

**Objective-C**:

```objc
float newSrcData[2] = {101, 105};
float data[8] = {10, 20, 30, 40, 50, 60, 70, 80};

vImage_Buffer newSrcBuf = {
    .data = newSrcData,
    .width = 1,
    .height = 2,
    .rowBytes = 4
};

vImage_Buffer buf = {
    .data = data,
    .width = 1,
    .height = 2,
    .rowBytes = 16
};

vImageOverwriteChannels_ARGBFFFF(&newSrcBuf,
                                  &buf,
                                  &buf,
                                  0x8,
                                  kvImageNoFlags);

// Prints "[101, 20, 30, 40, 105, 60, 70, 80]".
printf("[%g, %g, %g, %g, %g, %g, %g, %g]\n",
       data[0], data[1], data[2], data[3],
       data[4], data[5], data[6], data[7]);
```

## Parameters

- `newSrc`: The source vImage buffer that provides the new channel values.
- `origSrc`: The source vImage buffer that provides the original pixel values.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `copyMask`: A bitmask that specifies the channel or channels that the function overwrites with the corresponding channel in the `newSrc` parameter. The value `0x8` represents channel `0`, the value `0x4` represents channel `1`, the value `0x2` represents channel `2`, and the value `0x1` represents channel `3`.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Overwriting with another buffer
- [func vImageSelectChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](./vimageselectchannels_argb8888%28_,_,_,_,_%29.md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the specified channels of the corresponding pixels of a second buffer.
- [func vImageSelectChannels_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](./vimageselectchannels_argbffff%28_,_,_,_,_%29.md)
  Overwrites the channels of a floating-point 32-bit-per-channel, 4-channel interleaved buffer with the specified channels of the corresponding pixels of a second buffer.
- [func vImageOverwriteChannels_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, UInt8, vImage_Flags) -> vImage_Error](./vimageoverwritechannels_argb8888%28_,_,_,_,_%29.md)
  Overwrites the channels of an 8-bit-per-channel, 4-channel interleaved buffer with the corresponding pixels of a planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageoverwritechannels_argbffff(_:_:_:_:_:))*