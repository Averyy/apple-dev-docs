# containsMipmaps

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that states whether the loaded texture contains mip maps.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var containsMipmaps: Bool { get }
```

```objc
@property (readonly) BOOL containsMipmaps;
```

## See Also

### Reading Texture Information
- [var name: GLuint](./name-swift.property.md)
  The OpenGL context’s name for the texture.
- [var target: GLenum](./target-swift.property.md)
  The OpenGL binding target for the texture.
- [var height: GLuint](./height-swift.property.md)
  The height of the loaded texture.
- [var width: GLuint](./width-swift.property.md)
  The width of the loaded texture.
- [var textureOrigin: GLKTextureInfoOrigin](./textureorigin-swift.property.md)
  The location of the origin in the loaded texture.
- [var alphaState: GLKTextureInfoAlphaState](./alphastate-swift.property.md)
  The state of the alpha component in the loaded texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfo/containsmipmaps-swift.property)*