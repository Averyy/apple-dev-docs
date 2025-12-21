# CVImageBufferIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func

Returns a Boolean value indicating whether the image is vertically flipped.

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
func CVImageBufferIsFlipped(_ imageBuffer: CVImageBuffer) -> Bool
```

#### Return Value

Returns [`true`](https://developer.apple.com/documentation/Swift/true) if `{0,0}` represents the upper left of the image, or [`false`](https://developer.apple.com/documentation/Swift/false) if `{0,0}` represents the lower left of the image.

## Parameters

- `imageBuffer`: An image buffer.

## See Also

- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](cvimagebuffergetcleanrect(_:).md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](cvimagebuffergetcolorspace(_:).md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](cvimagebuffergetdisplaysize(_:).md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](cvimagebuffergetencodedsize(_:).md)
  Returns the full encoded dimensions of a Core Video image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferisflipped(_:))*