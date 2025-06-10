# withUnsafeBufferPointer(_:)

**Framework**: Accelerate  
**Kind**: method

Calls the given closure with a pointer to the buffer’s contiguous storage.

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
func withUnsafeBufferPointer<R>(_ body: (UnsafeBufferPointer<Format.ComponentType>) throws -> R) rethrows -> R
```

#### Return Value

The return value, if any, of the body closure parameter.

#### Discussion

You can use this function to simplify interoperation with other libraries and frameworks. For example, the following code uses Accelerate’s [`vForce`](vforce-library.md) library to raise each pixel value to the power of `1 / 2.2`:

```swift
let srcBuffer = vImage.PixelBuffer(pixelValues: [0.1, 0.2, 0.3, 0.4],
                                   size: vImage.Size(width: 4, height: 1),
                                   pixelFormat: vImage.PlanarF.self)

let destBuffer =  vImage.PixelBuffer(size: srcBuffer.size,
                                     pixelFormat: vImage.PlanarF.self)

var exponent = Float(1 / 2.2)
var count = Int32(4)

srcBuffer.withUnsafeBufferPointer { src in
    destBuffer.withUnsafeMutableBufferPointer { dest in
        
        vvpowsf(dest.baseAddress!,
                &exponent,
                src.baseAddress!,
                &count)
    }
}
```

> **Note**:  The contiguous storage may include space outside of the buffer’s width that doesn’t contain image information. The storage contains `rowStride * channelCount * height` elements.

## Parameters

- `body`: A closure with an   parameter that points to the contiguous storage for the pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/vimage/pixelbuffer/withunsafebufferpointer(_:))*