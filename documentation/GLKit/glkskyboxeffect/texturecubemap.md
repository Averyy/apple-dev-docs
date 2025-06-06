# textureCubeMap

**Framework**: GLKit  
**Kind**: property

The texture to apply to the skybox.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var textureCubeMap: GLKEffectPropertyTexture { get }
```

#### Discussion

Your application should create a complete texture cube map in its initialization code. Then, assign the name of this texture to the [`textureCubeMap`](glkskyboxeffect/texturecubemap.md) property of the skybox object.

```objc
skyboxEffect.textureCubeMap.glName = texture_name;
```

## See Also

- [var center: GLKVector3](glkskyboxeffect/center.md)
  The center of the skybox.
- [var xSize: GLfloat](glkskyboxeffect/xsize.md)
  The width of the skybox.
- [var ySize: GLfloat](glkskyboxeffect/ysize.md)
  The height of the skybox.
- [var zSize: GLfloat](glkskyboxeffect/zsize.md)
  The depth of the skybox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkskyboxeffect/texturecubemap)*