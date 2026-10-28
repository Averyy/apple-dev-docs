# textureCubeMap

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The texture map to apply in the reflection stage.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var textureCubeMap: GLKEffectPropertyTexture { get }
```

```objc
@property (nonatomic, readonly) GLKEffectPropertyTexture * textureCubeMap;
```

## Discussion

Your application should create a complete texture cube map in its initialization code. Then, assign the name of this texture to the [`textureCubeMap`](./texturecubemap.md) property.

```objc
reflectionMapObject.textureCubeMap.glName = texture_name;
```

## See Also

### Effect Properties
- [var matrix: GLKMatrix3](./matrix.md)
  The reflection matrix to apply to the normals of the submitted vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/texturecubemap)*