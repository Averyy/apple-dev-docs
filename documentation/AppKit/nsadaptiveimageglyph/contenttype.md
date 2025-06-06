# contentType

**Framework**: AppKit  
**Kind**: property

The image data format to use for this image type.

**Availability**:
- macOS 15.0+

## Declaration

```swift
class var contentType: UTType { get }
```

#### Discussion

Use this type when you need to specify the type of the image data. Adaptive images are compatible with the HEIC format, but include extra metadata about the supported resolutions and sizes.

## See Also

- [var contentIdentifier: String](nsadaptiveimageglyph/contentidentifier.md)
  A unique identifier for this image.
- [var contentDescription: String](nsadaptiveimageglyph/contentdescription.md)
  An alternate textual description of the image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsadaptiveimageglyph/contenttype)*