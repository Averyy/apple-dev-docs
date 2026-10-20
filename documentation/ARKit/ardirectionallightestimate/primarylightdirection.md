# primaryLightDirection

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A vector indicating the orientation of the strongest directional light source in the scene.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var primaryLightDirection: simd_float3 { get }
```

```objc
@property (nonatomic, readonly) simd_float3 primaryLightDirection;
```

#### Discussion

When ARKit analyzes the directional lighting environment for a detected face, the resulting lighting estimate can represent the influence of multiple light sources with different directions and intensities. To access this level of detail for use in your custom rendering code, use the [`sphericalHarmonicsCoefficients`](./sphericalharmonicscoefficients.md) property.

If your app displays AR content using a technology that doesn’t support environment-based lighting, this [`primaryLightDirection`](./primarylightdirection.md) property represents the average of directional light sources in the scene. This vector is normalized and in world coordinate space.

## See Also

### Examining Light Parameters
- [var sphericalHarmonicsCoefficients: Data](./sphericalharmonicscoefficients.md)
  Data describing the estimated lighting environment in all directions.
- [var primaryLightIntensity: CGFloat](./primarylightintensity.md)
  The estimated intensity, in lumens, of the strongest directional light source in the scene.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ardirectionallightestimate/primarylightdirection)*