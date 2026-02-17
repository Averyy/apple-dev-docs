# withUnsafeBytes(as:_:)

**Framework**: Swift Testing  
**Kind**: method  
**Required**: Yes

Encode a representation of this image in a given image format.

**Availability**:
- Swift 6.3+
- Xcode 26.4+ (Beta)

## Declaration

```swift
borrowing func withUnsafeBytes<R>(as imageFormat: AttachableImageFormat, _ body: (UnsafeRawBufferPointer) throws -> R) throws -> R
```

#### Return Value

Whatever is returned by `body`.

#### Discussion

> **Note**: Whatever is thrown by `body`, or any error that prevented the creation of the buffer.

The testing library uses this function when saving an image as an attachment. The implementation should use `imageFormat` to determine what encoder to use.

## Parameters

- `imageFormat`: The image format to use when encoding this image.
- `body`: A function to call. A temporary buffer containing a data   representation of this instance is passed to it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/testing/attachableasimage/withunsafebytes(as:_:))*