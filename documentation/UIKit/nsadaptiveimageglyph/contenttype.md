# contentType

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The image data format to use for this image type.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class var contentType: UTType { get }
```

```objc
@property (class, readonly) UTType * contentType;
```

## Discussion

Use this type when you need to specify the type of the image data. Adaptive images are compatible with the HEIC format, but include extra metadata about the supported resolutions and sizes.

## See Also

### Getting the content metadata
- [var contentIdentifier: String](./contentidentifier.md)
  A unique identifier for this image.
- [var contentDescription: String](./contentdescription.md)
  An alternate textual description of the image contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/contenttype)*