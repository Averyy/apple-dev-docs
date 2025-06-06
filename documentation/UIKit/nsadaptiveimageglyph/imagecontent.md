# imageContent

**Framework**: UIKit  
**Kind**: property

The raw data for the image.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
var imageContent: Data { get }
```

#### Discussion

This property contains the image data, the unique identifier for the image, the image description, and additional metadata. When saving your content to disk, save the data for any adaptive images with the rest of your content. If you need to specify a type for the image data, use the value in the [`contentType`](nsadaptiveimageglyph/contenttype.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsadaptiveimageglyph/imagecontent)*