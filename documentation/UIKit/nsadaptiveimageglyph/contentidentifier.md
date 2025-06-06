# contentIdentifier

**Framework**: UIKit  
**Kind**: property

A unique identifier for this image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var contentIdentifier: String { get }
```

#### Discussion

Use this property to create a persistent reference to this specific image in your code. The image data contains this content identifier, so the value persists between instantiations.

## See Also

- [var contentDescription: String](nsadaptiveimageglyph/contentdescription.md)
  An alternate textual description of the image contents.
- [class var contentType: UTType](nsadaptiveimageglyph/contenttype.md)
  The image data format to use for this image type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/contentidentifier)*