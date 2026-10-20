# lightModelAmbientColor

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

The ambient color applied to all primitives rendered by the effect.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var lightModelAmbientColor: GLKVector4 { get set }
```

```objc
@property (nonatomic, assign) GLKVector4 lightModelAmbientColor;
```

## See Also

### Configuring Lights
- [var lightingType: GLKLightingType](./lightingtype.md)
  The strategy the effect uses to calculate light values at each fragment. See [`GLKLightingType`](../glklightingtype.md).
- [var lightModelTwoSided: GLboolean](./lightmodeltwosided.md)
  A Boolean value that indicates whether lighting is calculated for both sides of a primitive.
- [var material: GLKEffectPropertyMaterial](./material.md)
  The material properties used when calculating the light values for a rendered primitive.
- [var light0: GLKEffectPropertyLight](./light0.md)
  The lighting properties for the first light in the scene.
- [var light1: GLKEffectPropertyLight](./light1.md)
  The lighting properties for the second light in the scene.
- [var light2: GLKEffectPropertyLight](./light2.md)
  The lighting properties for the third light in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkbaseeffect/lightmodelambientcolor)*