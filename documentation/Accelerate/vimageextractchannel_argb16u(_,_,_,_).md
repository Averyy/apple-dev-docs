# vImageExtractChannel_ARGB16U(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Extracts a single channel from an unsigned 16-bit-per-channel, 4-channel interleaved buffer and writes the result to an unsigned 16-bit planar buffer.

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
func vImageExtractChannel_ARGB16U(_ src: UnsafePointer<vImage_Buffer>, _ dest: UnsafePointer<vImage_Buffer>, _ channelIndex: Int, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageExtractChannel_ARGB16U(const vImage_Buffer *src, const vImage_Buffer *dest, long channelIndex, vImage_Flags flags);
```

## Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

## Discussion

The following code extracts channel `1` from the source buffer and writes the result to the destination buffer:

**Swift**:

```swift
let source = vImage.PixelBuffer<vImage.Interleaved16Ux4>(
    pixelValues: [10, 20, 30, 40,
                  50, 60, 70, 80],
    size: .init(width: 1, height: 2))

let destination = vImage.PixelBuffer<vImage.Planar16U>(
    size: source.size
)

source.withUnsafePointerToVImageBuffer { src in
    destination.withUnsafePointerToVImageBuffer { dst in
        _ = vImageExtractChannel_ARGB16U(src,
                                          dst,
                                          1,
                                          vImage_Flags(kvImageNoFlags))
    }
}

// Prints:
//      "[20,
//        60]".
print(destination.array)
```

**Objective-C**:

```objc
uint16_t src[8] = {10, 20, 30, 40,  50, 60, 70, 80};
uint16_t dst[2] = {0, 0};

vImage_Buffer srcBuf = {
    .data = src,
    .width = 1,
    .height = 2,
    .rowBytes = 8
};

vImage_Buffer dstBuf = {
    .data = dst,
    .width = 1,
    .height = 2,
    .rowBytes = 2
};

vImageExtractChannel_ARGB16U(&srcBuf,
                             &dstBuf,
                             1,
                             kvImageNoFlags);

// Prints "[20, 60]".
printf("[%d, %d]\n", dst[0], dst[1]);
```

## Parameters

- `src`: The source vImage buffer.
- `dest`: A pointer to the destination vImage buffer structure. You’re responsible for filling out the [`height`](./vimage_buffer/height.md), [`width`](./vimage_buffer/width.md), and [`rowBytes`](./vimage_buffer/rowbytes.md) fields of this structure, and for allocating a data buffer of the appropriate size. On return, the data buffer this structure points to contains the destination image data. When you no longer need the data buffer, deallocate the memory to prevent memory leaks.
- `channelIndex`: The index of the channel that the function extracts.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).

## See Also

### Extracting channels
- [func vImageExtractChannel_ARGB8888(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error](./vimageextractchannel_argb8888%28_,_,_,_%29.md)
  Extracts a single channel from an 8-bit-per-channel, 4-channel interleaved buffer and writes the result to an 8-bit planar buffer.
- [func vImageExtractChannel_ARGBFFFF(UnsafePointer<vImage_Buffer>, UnsafePointer<vImage_Buffer>, Int, vImage_Flags) -> vImage_Error](./vimageextractchannel_argbffff%28_,_,_,_%29.md)
  Extracts a single channel from a 32-bit-per-channel, 4-channel interleaved buffer and writes the result to a 32-bit planar buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageextractchannel_argb16u(_:_:_:_:))*