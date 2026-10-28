# target

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The OpenGL binding target for the texture.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var target: GLenum { get }
```

```objc
@property (readonly) GLenum target;
```

## Discussion

Your app uses this property as the target value when it binds the texture to a context.

## See Also

### Reading Texture Information
- [var name: GLuint](./name-swift.property.md)
  The OpenGL context’s name for the texture.
- [var height: GLuint](./height-swift.property.md)
  The height of the loaded texture.
- [var width: GLuint](./width-swift.property.md)
  The width of the loaded texture.
- [var textureOrigin: GLKTextureInfoOrigin](./textureorigin-swift.property.md)
  The location of the origin in the loaded texture.
- [var alphaState: GLKTextureInfoAlphaState](./alphastate-swift.property.md)
  The state of the alpha component in the loaded texture.
- [var containsMipmaps: Bool](./containsmipmaps-swift.property.md)
  A Boolean value that states whether the loaded texture contains mip maps.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfo/target-swift.property)*