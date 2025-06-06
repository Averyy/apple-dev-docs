# sphericalHarmonicsCoefficients

**Framework**: ARKit  
**Kind**: property

Data describing the estimated lighting environment in all directions.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var sphericalHarmonicsCoefficients: Data { get }
```

#### Discussion

Spherical harmonics provide a compact mathematical model for the global lighting environment around a point in space, describing the distribution and colors of multiple directional light sources. When used in a renderer that supports environment-based lighting, spherical harmonics provide much less high-frequency detail than a cube map texture, but make much more efficient use of GPU resources.

ARKit provides second-level spherical harmonics in separate red, green, and blue data planes. Thus, this data buffer contains 3 sets of 9 coefficients, or a total of 27 values of 32-bit floating point type.

## See Also

- [var primaryLightDirection: simd_float3](ardirectionallightestimate/primarylightdirection.md)
  A vector indicating the orientation of the strongest directional light source in the scene.
- [var primaryLightIntensity: CGFloat](ardirectionallightestimate/primarylightintensity.md)
  The estimated intensity, in lumens, of the strongest directional light source in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardirectionallightestimate/sphericalharmonicscoefficients)*