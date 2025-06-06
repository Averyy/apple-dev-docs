# textureCubeMap

**Framework**: GLKit  
**Kind**: property

The texture map to apply in the reflection stage.

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

Your application should create a complete texture cube map in its initialization code. Then, assign the name of this texture to the [`textureCubeMap`](glkreflectionmapeffect/texturecubemap.md) property.

```objc
reflectionMapObject.textureCubeMap.glName = texture_name;
```

## See Also

- [var matrix: GLKMatrix3](glkreflectionmapeffect/matrix.md)
  The reflection matrix to apply to the normals of the submitted vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkreflectionmapeffect/texturecubemap)*