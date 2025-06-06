# reflectiveTexture

**Framework**: Model I/O  
**Kind**: property

A cube map texture that contains a rendering of a scene as seen from the light probe’s position.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var reflectiveTexture: MDLTexture? { get }
```

#### Discussion

A reflective texture is also known as an . A renderer can use this texture to create reflections and specular highlights on surfaces with metallic materials.

## See Also

- [var irradianceTexture: MDLTexture?](mdllightprobe/irradiancetexture.md)
  A cube map texture that contains samples of the total light arriving at the light probe’s position from every direction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdllightprobe/reflectivetexture)*