# sunElevation

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) float sunElevation;
```

## Discussion

An elevation of `1.0` places the sun at the zenith (the center of the top face of the cube texture), a value of `0.0` places the sun at the nadir (the center of the bottom face), and a value of `0.5` places the sun on the horizon. The azimuth angle of the sun is fixed; to control the horizontal position of the sun relative to scene content, rotate the scene element responsible for displaying the sky cube texture.

Combine changes to this property with different [`turbidity`](./turbidity.md) and [`upperAtmosphereScattering`](./upperatmospherescattering.md) to create sunset, dawn, or twilight effects.

## See Also

### Working with Sky Simulation Parameters
- [var turbidity: Float](./turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var upperAtmosphereScattering: Float](./upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](./groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](./groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](./horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/sunelevation)*