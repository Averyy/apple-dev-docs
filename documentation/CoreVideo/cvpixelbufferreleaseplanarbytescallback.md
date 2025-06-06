# CVPixelBufferReleasePlanarBytesCallback

**Framework**: Core Video  
**Kind**: typealias

Defines a pointer to a pixel buffer release callback function, which is called when a pixel buffer created by [`CVPixelBufferCreateWithPlanarBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) is released.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
typealias CVPixelBufferReleasePlanarBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?) -> Void
```

#### Discussion

You would declare a callback named `MyPixelBufferReleasePlanarBytes` like this:

##### Discussion

You use this callback to release the pixels and perform any other cleanup when a pixel buffer is released.

## Parameters

- `releaseRefCon`: A pointer to application-defined data. This pointer is the same as that passed in the   parameter of  .
- `dataPtr`: A pointer to a plane descriptor block. This is the same pointer you passed to   in the   parameter.
- `dataSize`: The size value you passed to   in the   parameter.
- `numberOfPlanes`: The number of planes value you passed to   in the   parameter.
- `planeAddresses`: A pointer to the base plane address you passed to   in the   parameter.

## See Also

- [typealias CVPixelBufferReleaseBytesCallback](cvpixelbufferreleasebytescallback.md)
  A type that defines a release callback function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleaseplanarbytescallback)*