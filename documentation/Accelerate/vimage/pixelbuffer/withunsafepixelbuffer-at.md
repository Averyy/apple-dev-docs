# withUnsafePixelBuffer(at:_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with the pixel buffer that references the individual plane at the given index.

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
func withUnsafePixelBuffer<R>(at index: Int, _ body: (vImage.PixelBuffer<Format.PlanarPixelFormat>) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

Use this function to access a single planar pixel buffer from a multiple-plane pixel buffer. For example, the following code converts the 8-bit pixels at plane `2` to 32-bit and writes the result to `dest`:

```swift
 let src = vImage.PixelBuffer<vImage.Planar8x4>(size: vImage.Size(width: 32,
                                                                  height: 64))

 let dest = vImage.PixelBuffer<vImage.PlanarF>(size: src.size)

 src.withUnsafePixelBuffer(at: 2) { vImageBuffer in

     vImageBuffer.convert(to: dest)
 }
```

## Parameters

- `index`: The index of the plane.
- `body`: A closure with a   parameter that points to the underlying pixel buffer at the given index.

## See Also

- [func withUnsafePixelBuffers<R>(([vImage.PixelBuffer<Format.PlanarPixelFormat>]) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafepixelbuffers(_:).md)
  Calls the given closure with the array of pixel buffers that reference the individual planes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafepixelbuffer(at:_:))*