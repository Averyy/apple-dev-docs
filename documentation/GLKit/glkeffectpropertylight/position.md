# position

**Framework**: GLKit  
**Kind**: property

The position of the light in world coordinates.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var position: GLKVector4 { get set }
```

#### Discussion

If the `w` component of the position is `0.0`, the light is calculated using the directional light formula. The `x`, `y`, and `z` components of the vector specify the direction the light shines. The light is assumed to be infinitely far away; attenuation and spotlight properties are ignored.

If the `w` component of the position is a non-zero value, the coordinates specify the position of the light in homogenous coordinates, and the light is either calculated as a point light or a spotlight, depending on the value of the [`spotCutoff`](glkeffectpropertylight/spotcutoff.md) property.

The default value is `[0.0, 0.0, 1.0, 0.0]`.

## See Also

- [var enabled: GLboolean](glkeffectpropertylight/enabled.md)
  A Boolean value that indicates whether calculations should be performed on this light.
- [var transform: GLKEffectPropertyTransform](glkeffectpropertylight/transform.md)
  A transform applied to the light’s position and direction before calculating the contribution of the light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/position)*