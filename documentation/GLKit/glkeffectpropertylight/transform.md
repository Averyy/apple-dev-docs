# transform

**Framework**: GLKit  
**Kind**: property

A transform applied to the light’s position and direction before calculating the contribution of the light.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var transform: GLKEffectPropertyTransform { get set }
```

#### Discussion

The default value is the identity matrix.

## See Also

- [var enabled: GLboolean](glkeffectpropertylight/enabled.md)
  A Boolean value that indicates whether calculations should be performed on this light.
- [var position: GLKVector4](glkeffectpropertylight/position.md)
  The position of the light in world coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/transform)*