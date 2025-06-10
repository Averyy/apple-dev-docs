# withUnsafeVImageBuffers(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with the underlying vImage buffers.

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
func withUnsafeVImageBuffers<R>(_ body: ([vImage_Buffer]) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

Use this function to incorporate pixel buffer based image processing code with existing vImage code. For example, the following code accesses each multiple-plane pixel buffer’s underlying vImage buffers’ `rowBytes` property:

```swift
 let src = vImage.PixelBuffer<vImage.Planar8x4>(size: vImage.Size(width: 32,
                                                                 height: 64))

 src.withUnsafeVImageBuffers { vImageBuffers in
    for buffer in vImageBuffers {
        print(buffer.rowBytes)
     }
 }
```

## Parameters

- `body`: A closure with a   parameter that points to the underlying vImage buffers of the pixel buffer.

## See Also

- [func withUnsafePointerToVImageBuffer<R>((UnsafePointer<vImage_Buffer>) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafepointertovimagebuffer(_:).md)
  Calls the given closure with an unsafe pointer to the underlying vImage buffer.
- [func withUnsafeVImageBuffer<R>((vImage_Buffer) throws -> R) rethrows -> R](vimage/pixelbuffer/withunsafevimagebuffer(_:).md)
  Calls the given closure with the underlying vImage buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafevimagebuffers(_:))*