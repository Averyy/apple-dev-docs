# CVPixelBufferReleaseBytesCallback

**Framework**: Core Video  
**Kind**: typealias

A type that defines a release callback function.

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
typealias CVPixelBufferReleaseBytesCallback = (UnsafeMutableRawPointer?, UnsafeRawPointer?) -> Void
```

#### Discussion

When you create a pixel buffer using [`CVPixelBufferCreateWithBytes(_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md), you can optionally pass a callback function that’s invoked when the system frees the pixel buffer. Use this callback function to release the pixel data and perform any other cleanup needed when the buffer is released.

You define a callback function as shown below:

**Swift**:

```swift
// Define a function to call when the pixel buffer is freed.
let releaseCallback: CVPixelBufferReleaseBytesCallback = { releaseRefCon, baseAddress in
    guard let baseAddress = baseAddress else { return }
    free(UnsafeMutableRawPointer(mutating: baseAddress))
    // Perform additional cleanup as needed.
}
```

**Objective-C**:

```objc
// Define a function to call when the pixel buffer is freed.
void releaseCallback(void *releaseRefCon, const void *baseAddress) {
    free((void *)baseAddress);
    // Perform additional cleanup as needed.
}
```

## Parameters

- `releaseRefCon`: A pointer to application-defined data. This pointer is the same as that passed in the `releaseRefCon` parameter of [`CVPixelBufferCreateWithBytes(_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md).
- `baseAddress`: A pointer to the base address of the memory holding the pixels. This pointer is the same as that passed in the `baseAddress` parameter of [`CVPixelBufferCreateWithBytes(_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithbytes(_:_:_:_:_:_:_:_:_:_:).md).

## See Also

- [typealias CVPixelBufferReleasePlanarBytesCallback](cvpixelbufferreleaseplanarbytescallback.md)
  Defines a pointer to a pixel buffer release callback function, which is called when a pixel buffer created by [`CVPixelBufferCreateWithPlanarBytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:)`](cvpixelbuffercreatewithplanarbytes(_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:).md) is released.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvpixelbufferreleasebytescallback)*