# upperAtmosphereScattering

**Framework**: Model I/O  
**Kind**: property

A factor that influences the color of the simulated sky.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var upperAtmosphereScattering: Float { get set }
```

#### Discussion

This value affects the intensity of sunlight and the color of the sky. A value of `0.0` produces muted, dusky colors, and a value of 1.0 produces saturated, noon-like sky colors.

## See Also

- [var turbidity: Float](mdlskycubetexture/turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var sunElevation: Float](mdlskycubetexture/sunelevation.md)
  The sun’s position in the simulated sky.
- [var groundAlbedo: Float](mdlskycubetexture/groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](mdlskycubetexture/groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](mdlskycubetexture/horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/upperatmospherescattering)*