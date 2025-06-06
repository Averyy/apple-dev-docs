# constantAttenuation

**Framework**: GLKit  
**Kind**: property

A constant factor applied to the attenuation of a point light or spotlight.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- macOS 10.8+
- tvOS 9.0+

## Declaration

```swift
var constantAttenuation: GLfloat { get set }
```

#### Discussion

The distance attenuation factor is calculated as `1.0 / (k0 + k1 * d + k2 * d * d)`, where `d` represents the distance from the light to the point being lit. The [`constantAttenuation`](glkeffectpropertylight/constantattenuation.md) property is represented in this calculation as `k0`. The default value is `1.0`.

## See Also

- [var linearAttenuation: GLfloat](glkeffectpropertylight/linearattenuation.md)
  A linear factor applied to the attenuation of a point light or spotlight.
- [var quadraticAttenuation: GLfloat](glkeffectpropertylight/quadraticattenuation.md)
  A quadratic factor applied to the attenuation of a point light or spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/constantattenuation)*