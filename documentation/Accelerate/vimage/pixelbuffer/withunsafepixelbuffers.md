# withUnsafePixelBuffers(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with the array of pixel buffers that reference the individual planes.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
func withUnsafePixelBuffers<R>(_ body: ([vImage.PixelBuffer<Format.PlanarPixelFormat>]) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

Use this function to access each individual planar pixel buffer of a multiple-plane pixel buffer. For example, the following code initializes a 4-channel interleaved pixel buffer from the first three pixel buffers of a 4-channel multiple-plane pixel buffer:

```swift
 let src = vImage.PixelBuffer<vImage.Planar8x4>(size: vImage.Size(width: 32,
                                                                  height: 64))

 src.withUnsafePixelBuffers { overlaySource8x4PixelBuffers in

     let dest = vImage.PixelBuffer<vImage.Interleaved8x3>(planarBuffers: [
         overlaySource8x4PixelBuffers[0],
         overlaySource8x4PixelBuffers[1],
         overlaySource8x4PixelBuffers[2]
     ])
 }
```

## Parameters

- `body`: A closure with an array   parameter that points to the underlying pixel buffers.

## See Also

- [func withUnsafePixelBuffer<R>(at: Int, (vImage.PixelBuffer<Format.PlanarPixelFormat>) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafepixelbuffer(at:_:).md)
  Calls the given closure with the pixel buffer that references the individual plane at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafepixelbuffers(_:))*