# sunElevation

**Framework**: Model I/O  
**Kind**: property

The sun’s position in the simulated sky.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var sunElevation: Float { get set }
```

#### Discussion

An elevation of `1.0` places the sun at the zenith (the center of the top face of the cube texture), a value of `0.0` places the sun at the nadir (the center of the bottom face), and a value of `0.5` places the sun on the horizon. The azimuth angle of the sun is fixed; to control the horizontal position of the sun relative to scene content, rotate the scene element responsible for displaying the sky cube texture.

Combine changes to this property with different [`turbidity`](mdlskycubetexture/turbidity.md) and [`upperAtmosphereScattering`](mdlskycubetexture/upperatmospherescattering.md) to create sunset, dawn, or twilight effects.

## See Also

- [var turbidity: Float](mdlskycubetexture/turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var upperAtmosphereScattering: Float](mdlskycubetexture/upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](mdlskycubetexture/groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](mdlskycubetexture/groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](mdlskycubetexture/horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/sunelevation)*