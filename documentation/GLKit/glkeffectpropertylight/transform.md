# transform

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A transform applied to the light’s position and direction before calculating the contribution of the light.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var transform: GLKEffectPropertyTransform { get set }
```

```objc
@property (nonatomic, retain) GLKEffectPropertyTransform * transform;
```

#### Discussion

The default value is the identity matrix.

## See Also

### Configuring Common Lighting Properties
- [var enabled: GLboolean](./enabled.md)
  A Boolean value that indicates whether calculations should be performed on this light.
- [var position: GLKVector4](./position.md)
  The position of the light in world coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/transform)*