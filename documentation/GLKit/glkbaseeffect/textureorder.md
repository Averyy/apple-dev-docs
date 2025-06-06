# textureOrder

**Framework**: GLKit  
**Kind**: property

The order in which textures are applied to rendered primitives.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var textureOrder: [GLKEffectPropertyTexture]? { get set }
```

#### Discussion

The value of this property should be an array whose contents are all [`GLKEffectPropertyTexture`](glkeffectpropertytexture.md) objects provided by the effect. The order of these objects in the array determines the order in which the textures are applied in the shader. For example, to reverse the order that the textures are applied to a scene, your application would use the following code:

```objc
baseEffect.textureOrder = [NSArray arrayWithObjects: baseEffect.texture2d1, baseEffect.texture2d0, nil];
```

The default value is an array that executes the texture stages in increasing order, skipping any texture stages that are not enabled.

## See Also

- [var texture2d0: GLKEffectPropertyTexture](glkbaseeffect/texture2d0.md)
  The properties for the first texture.
- [var texture2d1: GLKEffectPropertyTexture](glkbaseeffect/texture2d1.md)
  The properties for the second texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/textureorder)*