# name

**Framework**: GLKit  
**Kind**: property

The OpenGL context’s name for the texture.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var name: GLuint { get }
```

#### Discussion

Your app uses this identifier whenever it wants to bind the texture to a context.

## See Also

- [var target: GLenum](glktextureinfo/target-swift.property.md)
  The OpenGL binding target for the texture.
- [var height: GLuint](glktextureinfo/height-swift.property.md)
  The height of the loaded texture.
- [var width: GLuint](glktextureinfo/width-swift.property.md)
  The width of the loaded texture.
- [var textureOrigin: GLKTextureInfoOrigin](glktextureinfo/textureorigin-swift.property.md)
  The location of the origin in the loaded texture.
- [var alphaState: GLKTextureInfoAlphaState](glktextureinfo/alphastate-swift.property.md)
  The state of the alpha component in the loaded texture.
- [var containsMipmaps: Bool](glktextureinfo/containsmipmaps-swift.property.md)
  A Boolean value that states whether the loaded texture contains mip maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfo/name-swift.property)*