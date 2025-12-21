# init(_:)

**Framework**: Core Video  
**Kind**: init

Creates a CVPixelBuffer with given attributes. It allocates the necessary memory based on the dimensions, pixel format and extended pixels described in the `CVPixelBuffer/Attributes`.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
init(_ attributes: CVPixelBufferCreationAttributes) throws
```

#### Discussion

It is preferable to use [`CVMutablePixelBuffer.Pool`](cvmutablepixelbuffer/pool.md) for allocating pixel buffers in an environment that creates and releases pixel buffers of the same type, i.e., matching Attributes, repeatedly. The pool efficiently reuses the pixel buffer memory and reduces memory fragmentation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvmutablepixelbuffer/init(_:))*