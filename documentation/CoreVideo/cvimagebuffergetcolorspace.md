# CVImageBufferGetColorSpace(_:)

**Framework**: Core Video  
**Kind**: func

Returns the color space of a Core Video image buffer.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CVImageBufferGetColorSpace(_ imageBuffer: CVImageBuffer) -> Unmanaged<CGColorSpace>?
```

#### Return Value

The color space of the image buffer, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if you pass a value for the image buffer that isn’t a [`CVImageBuffer`](cvimagebuffer.md) type.

## Parameters

- `imageBuffer`: The image buffer containing the color space to retrieve.

## See Also

- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](cvimagebuffergetcleanrect(_:).md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](cvimagebuffergetdisplaysize(_:).md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](cvimagebuffergetencodedsize(_:).md)
  Returns the full encoded dimensions of a Core Video image buffer.
- [func CVImageBufferIsFlipped(CVImageBuffer) -> Bool](cvimagebufferisflipped(_:).md)
  Returns a Boolean value indicating whether the image is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffergetcolorspace(_:))*