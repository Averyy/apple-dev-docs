# withUnsafePointerToVImageBuffer(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with an unsafe pointer to the underlying vImage buffer.

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
func withUnsafePointerToVImageBuffer<R>(_ body: (UnsafePointer<vImage_Buffer>) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

Use this function to incorporate pixel buffer based image processing code with existing vImage code. For example, the following code passes a pixel buffer to the C API [`vImageBufferFill_ARGB8888(_:_:_:)`](vimagebufferfill_argb8888(_:_:_:).md) routine:

```swift
 let src = vImage.PixelBuffer<vImage.Interleaved8x4>(size: vImage.Size(width: 128, height: 128))

 src.withUnsafePointerToVImageBuffer { vImageBufferPtr in
     _ = vImageBufferFill_ARGB8888(vImageBufferPtr,
                                   [0, 0, 0, 0],
                                   vImage_Flags(kvImageNoFlags))
 }
```

## Parameters

- `body`: A closure with an unsafe pointer to a   parameter that points to the underlying vImage buffer of the pixel buffer.

## See Also

- [func withUnsafeVImageBuffer<R>((vImage_Buffer) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafevimagebuffer(_:).md)
  Calls the given closure with the underlying vImage buffer.
- [func withUnsafeVImageBuffers<R>(([vImage_Buffer]) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafevimagebuffers(_:).md)
  Calls the given closure with the underlying vImage buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafepointertovimagebuffer(_:))*