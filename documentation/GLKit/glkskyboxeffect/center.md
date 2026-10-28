# center

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The center of the skybox.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var center: GLKVector3 { get set }
```

```objc
@property (nonatomic, assign) GLKVector3 center;
```

## Discussion

The property holds the `[x,y,z]` coordinates of the center of the skybox.

## See Also

### Configuring the Skybox
- [var textureCubeMap: GLKEffectPropertyTexture](./texturecubemap.md)
  The texture to apply to the skybox.
- [var xSize: GLfloat](./xsize.md)
  The width of the skybox.
- [var ySize: GLfloat](./ysize.md)
  The height of the skybox.
- [var zSize: GLfloat](./zsize.md)
  The depth of the skybox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkskyboxeffect/center)*