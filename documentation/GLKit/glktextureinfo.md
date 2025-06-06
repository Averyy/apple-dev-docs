# GLKTextureInfo

**Framework**: GLKit  
**Kind**: class

Information about OpenGL textures created by the [`GLKTextureLoader`](glktextureloader.md) class.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
class GLKTextureInfo
```

#### Overview

When your app loads textures using the [`GLKTextureLoader`](glktextureloader.md) class, the texture loader returns information about the textures using [`GLKTextureInfo`](glktextureinfo.md) objects. Your app never creates [`GLKTextureInfo`](glktextureinfo.md) objects directly.

## Topics

### Reading Texture Information
- [var name: GLuint](glktextureinfo/name-swift.property.md)
  The OpenGL context’s name for the texture.
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
### Constants
- [enum GLKTextureInfoAlphaState](glktextureinfoalphastate.md)
  Values that describe the alpha information stored in a source image’s pixel data.
- [enum GLKTextureInfoOrigin](glktextureinfoorigin.md)
  The location of the origin in the original source image.
### Instance Properties
- [var arrayLength: GLuint](glktextureinfo/arraylength-swift.property.md)
- [var depth: GLuint](glktextureinfo/depth-swift.property.md)
- [var mimapLevelCount: GLuint](glktextureinfo/mimaplevelcount-swift.property.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class GLKTextureLoader](glktextureloader.md)
  A utility class that simplifies loading OpenGL or OpenGL ES texture datas from a variety of image file formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glktextureinfo)*