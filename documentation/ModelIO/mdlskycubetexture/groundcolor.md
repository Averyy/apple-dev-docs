# groundColor

**Framework**: Model I/O  
**Kind**: property

The color of the simulated ground.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var groundColor: CGColor? { get set }
```

#### Discussion

By default, this property’s value is `nil`, causing Model I/O to render an infinite sky above and below. If you set this property to a color, Model I/O renders a solid color for all areas of the cube texture below the level specified in the [`horizonElevation`](mdlskycubetexture/horizonelevation.md) property.

## See Also

- [var turbidity: Float](mdlskycubetexture/turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var sunElevation: Float](mdlskycubetexture/sunelevation.md)
  The sun’s position in the simulated sky.
- [var upperAtmosphereScattering: Float](mdlskycubetexture/upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](mdlskycubetexture/groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var horizonElevation: Float](mdlskycubetexture/horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/groundcolor)*