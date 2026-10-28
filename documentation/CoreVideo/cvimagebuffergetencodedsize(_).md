# CVImageBufferGetEncodedSize(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

Returns the full encoded dimensions of a Core Video image buffer.

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
func CVImageBufferGetEncodedSize(_ imageBuffer: CVImageBuffer) -> CGSize
```

```c
extern CGSize CVImageBufferGetEncodedSize(CVImageBufferRef imageBuffer);
```

## Return Value

A [`CGSize`](../CoreFoundation/cgsize.md) structure defining the full encoded size of the image buffer. The size is zero if you pass a value for the image buffer that isn’t a [`CVImageBuffer`](./cvimagebuffer.md) type.

## Discussion

For example, for an NTSC DV frame, this function returns an encoded size of 720 x 480. When you create a [`CIImage`](../CoreImage/ciimage.md) object from a Core Video image buffer, use this call to retrieve the image size.

## Parameters

- `imageBuffer`: The image buffer containing the encoded size to retrieve.

## See Also

### Inspecting image buffers
- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](./cvimagebuffergetcleanrect%28_%29.md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](./cvimagebuffergetcolorspace%28_%29.md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](./cvimagebuffergetdisplaysize%28_%29.md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferIsFlipped(CVImageBuffer) -> Bool](./cvimagebufferisflipped%28_%29.md)
  Returns a Boolean value indicating whether the image is vertically flipped.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebuffergetencodedsize(_:))*