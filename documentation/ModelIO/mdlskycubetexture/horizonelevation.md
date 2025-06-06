# horizonElevation

**Framework**: Model I/O  
**Kind**: property

The angle, in radians relative to center, below which to render the ground color.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var horizonElevation: Float { get set }
```

#### Discussion

By default, Model I/O renders an infinite sky above and below. If you set the [`groundColor`](mdlskycubetexture/groundcolor.md) property, Model I/O renders a solid color for all areas of the cube texture below this elevation. An elevation of `0.0` renders a horizon at the center elevation of the sky cube; negative values lead to a lower horizon and positive values to a higher horizon.

## See Also

- [var turbidity: Float](mdlskycubetexture/turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var sunElevation: Float](mdlskycubetexture/sunelevation.md)
  The sun’s position in the simulated sky.
- [var upperAtmosphereScattering: Float](mdlskycubetexture/upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](mdlskycubetexture/groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](mdlskycubetexture/groundcolor.md)
  The color of the simulated ground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/horizonelevation)*