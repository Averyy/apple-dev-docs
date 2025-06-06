# turbidity

**Framework**: Model I/O  
**Kind**: property

The cloudiness or haziness of the simulated sky.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var turbidity: Float { get set }
```

#### Discussion

A value of `0.0` simulates a clear sky—that is, the sun has little effect on the color of the sky around it. Values closer to `1.0` simulate increasing amounts of dust and moisture in the sky, causing the sun’s color to spread across the atmosphere.

## See Also

- [var sunElevation: Float](mdlskycubetexture/sunelevation.md)
  The sun’s position in the simulated sky.
- [var upperAtmosphereScattering: Float](mdlskycubetexture/upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](mdlskycubetexture/groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](mdlskycubetexture/groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](mdlskycubetexture/horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/turbidity)*