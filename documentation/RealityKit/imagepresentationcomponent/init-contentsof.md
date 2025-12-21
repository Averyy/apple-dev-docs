# init(contentsOf:)

**Framework**: RealityKit  
**Kind**: init

Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image file URL.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(contentsOf url: URL) async throws
```

#### Discussion

> **Note**: Throws an error if it is not possible to load even a monoscopic texture from the image file.

## See Also

- [init(imageSource: CGImageSource) async throws](imagepresentationcomponent/init(imagesource:).md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/init(contentsof:))*