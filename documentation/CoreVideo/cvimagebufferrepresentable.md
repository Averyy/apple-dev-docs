# CVImageBufferRepresentable

**Framework**: Core Video  
**Kind**: protocol

CVImageBufferRepresentable protocol is a sealed protocol intended to be implemented by the types in CoreVideo framework. This protocol facilitates Swift types that wrap a value of CVImageBuffer type.

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
protocol CVImageBufferRepresentable : CVBufferRepresentable, ~Copyable
```

## Topics

### Instance Properties
- [var cleanRect: CGRect](cvimagebufferrepresentable/cleanrect.md)
  Source rectangle of a CVImageBuffer that represents the clean aperture of the buffer in encoded pixels. For example, an NTSC DV frame would return a CGRect with an origin of 8,0 and a size of 704,480. Note that the origin of this rect always the lower left corner. This is the same coordinate system as used by CoreImage.
- [var colorSpace: CGColorSpace?](cvimagebufferrepresentable/colorspace.md)
  Color space of the image if specified
- [var displaySize: CGSize](cvimagebufferrepresentable/displaysize.md)
  Nominal output display size (in square pixels) of a CVImageBuffer. For example, for an NTSC DV frame this would be 640x480
- [var encodedSize: CGSize](cvimagebufferrepresentable/encodedsize.md)
  Full encoded dimensions of a CVImageBuffer.  For example, for an NTSC DV frame this would be 720x480
- [var originPosition: CVImageBufferOriginPosition](cvimagebufferrepresentable/originposition.md)
  Position of {0, 0} coordinates in the image

## Relationships

### Inherits From
- [CVBufferRepresentable](cvbufferrepresentable.md)
### Inherited By
- [CVPixelBufferRepresentable](cvpixelbufferrepresentable.md)
### Conforming Types
- [CVMutablePixelBuffer](cvmutablepixelbuffer.md)
- [CVReadOnlyPixelBuffer](cvreadonlypixelbuffer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/corevideo/cvimagebufferrepresentable)*