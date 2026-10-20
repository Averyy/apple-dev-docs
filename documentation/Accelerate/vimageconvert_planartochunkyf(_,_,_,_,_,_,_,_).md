# vImageConvert_PlanarToChunkyF(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Interleaves the specifed number of floating-point 32-bit planar buffers into a floating-point 32 -bit-per-channel interleaved buffer.

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
func vImageConvert_PlanarToChunkyF(_ srcPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ destChannels: UnsafeMutablePointer<UnsafeMutableRawPointer?>, _ channelCount: UInt32, _ destStrideBytes: Int, _ destWidth: vImagePixelCount, _ destHeight: vImagePixelCount, _ destRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error
```

```c
vImage_Error vImageConvert_PlanarToChunkyF(const vImage_Buffer * srcPlanarBuffers[], void * destChannels[], unsigned int channelCount, size_t destStrideBytes, vImagePixelCount destWidth, vImagePixelCount destHeight, size_t destRowBytes, vImage_Flags flags);
```

#### Return Value

[`kvImageNoError`](./kvimagenoerror.md); otherwise, one of the error codes in [Data Types and Constants](./data-types-and-constants.md).

#### Discussion

Use this function to interleave formats that either aren’t supported by the vImage library or are only known at runtime.

The following code interleaves two 4 x 1 planar buffers into a 4 x 1 interleaved two-channel buffer:

**Swift**:

```swift
let width = 4
let height = 1
let size = vImage.Size(width: width,
                       height: height)

let cbBuffer = vImage.PixelBuffer(pixelValues: [10, 11, 12, 13],
                                  size: size,
                                  pixelFormat: vImage.PlanarF.self)

let crBuffer = vImage.PixelBuffer(pixelValues: [20, 21, 22, 23],
                                  size: size,
                                  pixelFormat: vImage.PlanarF.self)

let cbCrBuffer = vImage.PixelBuffer(size: size,
                                    pixelFormat: vImage.InterleavedFx2.self)

cbBuffer.withUnsafePointerToVImageBuffer { cb in
    crBuffer.withUnsafePointerToVImageBuffer { cr in
        cbCrBuffer.withUnsafeVImageBuffer { cbcr in
            
            var srcPlanarBuffers = [Optional(cb), Optional(cr)]
            var destChannels = [
                cbcr.data,
                cbcr.data.advanced(by: MemoryLayout<Pixel_F>.stride)
            ]
            
            let channelCount = 2
            
            _ = vImageConvert_PlanarToChunkyF(
                &srcPlanarBuffers,
                &destChannels,
                UInt32(channelCount),
                MemoryLayout<Pixel_F>.stride * channelCount,
                vImagePixelCount(width),
                vImagePixelCount(height),
                cbcr.rowBytes,
                vImage_Flags(kvImageNoFlags))
            
        }
    }
}

// Prints "[10.0, 20.0,   11.0, 21.0,   12.0, 22.0,   13.0, 23.0]".
print(cbCrBuffer.array)
```

**Objective-C**:

```objc
float cbData[4] = {10.0f, 11.0f, 12.0f, 13.0f};
float crData[4] = {20.0f, 21.0f, 22.0f, 23.0f};

vImage_Buffer cbBuf = {
    .data     = cbData,
    .width    = 4,
    .height   = 1,
    .rowBytes = 16
};

vImage_Buffer crBuf = {
    .data     = crData,
    .width    = 4,
    .height   = 1,
    .rowBytes = 16
};

float dst[8] = {0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f};

const vImage_Buffer *srcPlanarBuffers[2] = { &cbBuf, &crBuf };

void *destChannels[2] = {
    dst,
    (uint8_t *)dst + sizeof(float)
};

vImageConvert_PlanarToChunkyF(
    srcPlanarBuffers,
    destChannels,
    2,
    sizeof(float) * 2,
    4,
    1,
    4 * sizeof(float) * 2,
    kvImageNoFlags);

// Prints "[10.0, 20.0, 11.0, 21.0, 12.0, 22.0, 13.0, 23.0]".
printf("[%f, %f, %f, %f, %f, %f, %f, %f]\n",
       dst[0], dst[1], dst[2], dst[3],
       dst[4], dst[5], dst[6], dst[7]);
```

## Parameters

- `srcPlanarBuffers`: An array that contains `channelCount` source planar vImage buffers. Each source buffer must be the same height and width, but they may have different [`rowBytes`](./vimage_buffer/rowbytes.md) values.
- `destChannels`: An array that contains pointers to the start of each channel in the destination buffer.
- `channelCount`: The number of channels in the destination image.
- `destStrideBytes`: The number of bytes between consecutive pixels in a channel in the same row.
- `destWidth`: The width, in pixels, of the destination channels and the source planar buffers.
- `destHeight`: The height, in pixels, of the destination channels and the source planar buffers.
- `destRowBytes`: The distance, in bytes, between the corresponding pixels in consecutive rows in the destination buffer, including any unused space between them.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass [`kvImageDoNotTile`](./kvimagedonottile.md); otherwise, pass [`kvImageNoFlags`](./kvimagenoflags.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_planartochunkyf(_:_:_:_:_:_:_:_:))*