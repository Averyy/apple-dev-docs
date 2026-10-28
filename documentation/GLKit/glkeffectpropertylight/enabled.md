# enabled

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether calculations should be performed on this light.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var enabled: GLboolean { get set }
```

```objc
@property (nonatomic, assign) GLboolean enabled;
```

## Discussion

If the value of [`enabled`](./enabled.md) is `GL_TRUE`, then lighting calculations are performed for this light. If the value is `GL_FALSE`, this light is skipped when computing the fragment color.

## See Also

### Configuring Common Lighting Properties
- [var position: GLKVector4](./position.md)
  The position of the light in world coordinates.
- [var transform: GLKEffectPropertyTransform](./transform.md)
  A transform applied to the light’s position and direction before calculating the contribution of the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/enabled)*