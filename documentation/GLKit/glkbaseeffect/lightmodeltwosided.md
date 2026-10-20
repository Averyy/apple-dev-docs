# lightModelTwoSided

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether lighting is calculated for both sides of a primitive.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var lightModelTwoSided: GLboolean { get set }
```

```objc
@property (nonatomic, assign) GLboolean lightModelTwoSided;
```

#### Discussion

If the value is `GL_TRUE` and the back face of a primitive is being rendered, the lighting values are calculated by negating the surface normals for the primitive. If the value is `GL_FALSE`, then the facing of the primitive is ignored when performing the lighting calculation. The default value is `GL_FALSE`.

Setting the value of this property to `GL_TRUE` may impact performance. Only use two-sided lighting when either side of a primitive could theoretically be visible to the camera.

## See Also

### Configuring Lights
- [var lightingType: GLKLightingType](./lightingtype.md)
  The strategy the effect uses to calculate light values at each fragment. See [`GLKLightingType`](../glklightingtype.md).
- [var material: GLKEffectPropertyMaterial](./material.md)
  The material properties used when calculating the light values for a rendered primitive.
- [var lightModelAmbientColor: GLKVector4](./lightmodelambientcolor.md)
  The ambient color applied to all primitives rendered by the effect.
- [var light0: GLKEffectPropertyLight](./light0.md)
  The lighting properties for the first light in the scene.
- [var light1: GLKEffectPropertyLight](./light1.md)
  The lighting properties for the second light in the scene.
- [var light2: GLKEffectPropertyLight](./light2.md)
  The lighting properties for the third light in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/lightmodeltwosided)*