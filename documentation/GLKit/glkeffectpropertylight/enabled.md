# enabled

**Framework**: GLKit  
**Kind**: property

A Boolean value that indicates whether calculations should be performed on this light.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var enabled: GLboolean { get set }
```

#### Discussion

If the value of [`enabled`](glkeffectpropertylight/enabled.md) is `GL_TRUE`, then lighting calculations are performed for this light. If the value is `GL_FALSE`, this light is skipped when computing the fragment color.

## See Also

- [var position: GLKVector4](glkeffectpropertylight/position.md)
  The position of the light in world coordinates.
- [var transform: GLKEffectPropertyTransform](glkeffectpropertylight/transform.md)
  A transform applied to the light’s position and direction before calculating the contribution of the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/enabled)*