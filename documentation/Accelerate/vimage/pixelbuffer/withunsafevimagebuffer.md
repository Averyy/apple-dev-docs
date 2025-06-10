# withUnsafeVImageBuffer(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with the underlying vImage buffer.

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
func withUnsafeVImageBuffer<R>(_ body: (vImage_Buffer) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

Use this function to incorporate pixel buffer based image processing code with existing vImage code. For example, the following code accesses a pixel buffer’s underlying vImage buffer’s `rowBytes` property:

```swift
 let src = try vImage.PixelBuffer<vImage.Interleaved8x4>(cgImage: cgImage,
                                                         cgImageFormat: &cgImageFormat)

 src.withUnsafeVImageBuffer { vImageBuffer in
     print(vImageBuffer.rowBytes)
 }
```

## Parameters

- `body`: A closure with a   parameter that points to the underlying vImage buffer of the pixel buffer.

## See Also

- [func withUnsafePointerToVImageBuffer<R>((UnsafePointer<vImage_Buffer>) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafepointertovimagebuffer(_:).md)
  Calls the given closure with an unsafe pointer to the underlying vImage buffer.
- [func withUnsafeVImageBuffers<R>(([vImage_Buffer]) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafevimagebuffers(_:).md)
  Calls the given closure with the underlying vImage buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafevimagebuffer(_:))*