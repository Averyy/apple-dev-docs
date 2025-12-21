# init(imageSource:)

**Framework**: RealityKit  
**Kind**: init

Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image source.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(imageSource: CGImageSource) async throws
```

#### Discussion

> **Note**: Throws an error if it is not possible to load even a monoscopic texture from the image source.

## See Also

- [init(contentsOf: URL) async throws](imagepresentationcomponent/init(contentsof:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/init(imagesource:))*