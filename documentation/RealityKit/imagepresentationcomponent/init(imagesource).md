# init(imageSource:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image source.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
init(imageSource: CGImageSource) async throws
```

#### Discussion

> **Throws**: Throws an error if it is not possible to load even a monoscopic texture from the image source.

## See Also

### Creating a component from a 2D image or spatial photo
- [init(contentsOf: URL) async throws](./init%28contentsof%29.md)
  Creates a new component by loading a monoscopic texture and (if present) a pair of spatial textures from the provided image file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/imagepresentationcomponent/init(imagesource:))*