# CVImageBufferGetCleanRect(_:)

**Framework**: Core Video  
**Kind**: func

Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.

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
func CVImageBufferGetCleanRect(_ imageBuffer: CVImageBuffer) -> CGRect
```

#### Return Value

A [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) structure returning the nominal display size of the image buffer. The size is zero if you pass a value for the image buffer that isn’t a [`CVImageBuffer`](cvimagebuffer.md) type.

#### Discussion

The clean aperture size is smaller than the full size of the image. For example, for an NTSC DV frame, this function returns a [`CGRect`](https://developer.apple.com/documentation/CoreFoundation/CGRect) structure with an origin of `(8,0)` and a size of 704 x 480.

> **Note**:  The origin of this rectangle is always in the lower-left corner. This is the same coordinate system as that used by Quartz and Core Image.

## Parameters

- `imageBuffer`: The image buffer containing the clean aperture to retrieve.

## See Also

- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](cvimagebuffergetcolorspace(_:).md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](cvimagebuffergetdisplaysize(_:).md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](cvimagebuffergetencodedsize(_:).md)
  Returns the full encoded dimensions of a Core Video image buffer.
- [func CVImageBufferIsFlipped(CVImageBuffer) -> Bool](cvimagebufferisflipped(_:).md)
  Returns a Boolean value indicating whether the image is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffergetcleanrect(_:))*