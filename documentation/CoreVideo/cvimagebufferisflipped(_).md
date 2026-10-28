# CVImageBufferIsFlipped(_:)

**Framework**: Core Video  
**Kind**: func  
**Role**: Function

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

```c
extern Boolean CVImageBufferIsFlipped(CVImageBufferRef imageBuffer);
```

## Return Value

Returns [`true`](../Swift/true.md) if `{0,0}` represents the upper left of the image, or [`false`](../Swift/false.md) if `{0,0}` represents the lower left of the image.

## Parameters

- `imageBuffer`: An image buffer.

## See Also

### Inspecting image buffers
- [func CVImageBufferGetCleanRect(CVImageBuffer) -> CGRect](./cvimagebuffergetcleanrect%28_%29.md)
  Returns the source rectangle of a Core Video image buffer that represents the clean aperture of the buffer in encoded pixels.
- [func CVImageBufferGetColorSpace(CVImageBuffer) -> Unmanaged<CGColorSpace>?](./cvimagebuffergetcolorspace%28_%29.md)
  Returns the color space of a Core Video image buffer.
- [func CVImageBufferGetDisplaySize(CVImageBuffer) -> CGSize](./cvimagebuffergetdisplaysize%28_%29.md)
  Returns the nominal output display size, in square pixels, of a Core Video image buffer.
- [func CVImageBufferGetEncodedSize(CVImageBuffer) -> CGSize](./cvimagebuffergetencodedsize%28_%29.md)
  Returns the full encoded dimensions of a Core Video image buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferisflipped(_:))*