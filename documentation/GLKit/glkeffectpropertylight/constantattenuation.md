# constantAttenuation

**Framework**: GLKit  
**Kind**: property  
**Role**: Instance Property

A constant factor applied to the attenuation of a point light or spotlight.

**Availability**:
- iOS 5.0+ - Deprecated in 12.0
- iPadOS 5.0+ - Deprecated in 12.0
- macOS 10.8+ - Deprecated in 10.14
- tvOS 9.0+ - Deprecated in 12.0

> **Deprecated**: OpenGLES API deprecated. (Define GLES_SILENCE_DEPRECATION to silence these warnings)

## Declaration

```swift
var constantAttenuation: GLfloat { get set }
```

```objc
@property (nonatomic, assign) GLfloat constantAttenuation;
```

## Discussion

The distance attenuation factor is calculated as `1.0 / (k0 + k1 * d + k2 * d * d)`, where `d` represents the distance from the light to the point being lit. The [`constantAttenuation`](./constantattenuation.md) property is represented in this calculation as `k0`. The default value is `1.0`.

## See Also

### Configuring Lighting Attenuation
- [var linearAttenuation: GLfloat](./linearattenuation.md)
  A linear factor applied to the attenuation of a point light or spotlight.
- [var quadraticAttenuation: GLfloat](./quadraticattenuation.md)
  A quadratic factor applied to the attenuation of a point light or spotlight.


---

*[View on Apple Developer](https://developer.apple.com/documentation/glkit/glkeffectpropertylight/constantattenuation)*