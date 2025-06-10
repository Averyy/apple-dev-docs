# vImageConvert_ChunkyToPlanarF(_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Deinterleaves a floating-point 32-bit-per-channel interleaved buffer with an arbitrary number of channels into the corresponding number of 32-bit planar buffers.

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
func vImageConvert_ChunkyToPlanarF(_ srcChannels: UnsafeMutablePointer<UnsafeRawPointer?>, _ destPlanarBuffers: UnsafeMutablePointer<UnsafePointer<vImage_Buffer>?>, _ channelCount: UInt32, _ srcStrideBytes: Int, _ srcWidth: vImagePixelCount, _ srcHeight: vImagePixelCount, _ srcRowBytes: Int, _ flags: vImage_Flags) -> vImage_Error
```

#### Return Value

[`kvImageNoError`](kvimagenoerror.md); otherwise, one of the error codes in [`Data Types and Constants`](data-types-and-constants.md).

#### Discussion

Use this function to deinterleave formats that either aren’t supported by the vImage library or are only known at runtime.

The following code interleaves a 4 x 1 interleaved 2-channel buffer into two 4 x 1 planar buffers:

```swift
let width = 4
let height = 1
let size = vImage.Size(width: width,
                       height: height)

let cbCrBuffer = vImage.PixelBuffer(pixelValues: [10, 20,   11, 21,   12, 22,   13, 23],
                                    size: size,
                                    pixelFormat: vImage.InterleavedFx2.self)

let cbBuffer = vImage.PixelBuffer(size: size,
                                  pixelFormat: vImage.PlanarF.self)

let crBuffer = vImage.PixelBuffer(size: size,
                                  pixelFormat: vImage.PlanarF.self)

cbCrBuffer.withUnsafeVImageBuffer { cbcr in
    cbBuffer.withUnsafePointerToVImageBuffer { cb in
        crBuffer.withUnsafePointerToVImageBuffer { cr in
            
            var srcChannels = [
                UnsafeRawPointer(cbcr.data),
                UnsafeRawPointer(cbcr.data.advanced(by: MemoryLayout<Pixel_F>.stride))
            ]
            
            var dstPlanarBuffers = [Optional(cb), Optional(cr)]
            
            let channelCount = 2
            
            _ = vImageConvert_ChunkyToPlanarF(
                &srcChannels,
                &dstPlanarBuffers,
                UInt32(channelCount),
                MemoryLayout<Pixel_F>.stride * channelCount,
                vImagePixelCount(width),
                vImagePixelCount(height),
                cbcr.rowBytes,
                vImage_Flags(kvImageNoFlags))
            
        }
    }
}

// Prints "[10.0, 11.0,    12.0, 13.0]".
print(cbBuffer.array)

// Prints "[20.0, 21.0,    22.0, 23.0]".
print(crBuffer.array)
```

## Parameters

- `srcChannels`: An array that contains pointers to the start of each channel in the source buffer.
- `destPlanarBuffers`: An array that contains   destination planar vImage buffers. Each source buffer must be the same height and width, but they may have different   values.
- `channelCount`: The number of channels in the source image.
- `srcStrideBytes`: The number of bytes between consecutive pixels in a channel in the same row.
- `srcWidth`: The width, in pixels, of the source channels and the destination planar buffers.
- `srcHeight`: The height, in pixels, of the source channels and the destination planar buffers.
- `srcRowBytes`: The distance, in bytes, between the corresponding pixels in consecutive rows in the source buffer, including any unused space between them.
- `flags`: The options to use when performing the operation. If your code implements its own tiling or its own multithreading, pass  ; otherwise, pass  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimageconvert_chunkytoplanarf(_:_:_:_:_:_:_:_:))*