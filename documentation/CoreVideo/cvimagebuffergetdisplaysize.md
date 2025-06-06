# CVImageBufferGetDisplaySize(_:)

**Framework**: Core Video  
**Kind**: func

Returns the nominal output display size, in square pixels, of a Core Video image buffer.

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
func CVImageBufferGetDisplaySize(_ imageBuffer: CVImageBuffer) -> CGSize
```

#### Return Value

A [`CGSize`](https://developer.apple.com/documentation/CoreFoundation/CGSize) structure defining the nominal display size of the image buffer. The size is zero if you pass a value for the image buffer that isn’t a [`CVImageBuffer`](cvimagebuffer.md) type.

#### Discussion

For example, for an NTSC DV frame, this function returns a size of 640 x 480.

## Parameters

- `imageBuffer`: The image buffer containing the display size to retrieve.

## See Also

- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](cvimagebuffergetcleanrect(_:).md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](cvimagebuffergetcolorspace(_:).md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](cvimagebuffergetencodedsize(_:).md)
  Returns the full encoded dimensions of a Core Video image buffer.
- [func CVImageBufferIsFlipped(CVImageBuffer) -> Bool](cvimagebufferisflipped(_:).md)
  Returns a Boolean value indicating whether the image is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffergetdisplaysize(_:))*