# turbidity

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, assign) float turbidity;
```

#### Discussion

A value of `0.0` simulates a clear sky—that is, the sun has little effect on the color of the sky around it. Values closer to `1.0` simulate increasing amounts of dust and moisture in the sky, causing the sun’s color to spread across the atmosphere.

## See Also

### Working with Sky Simulation Parameters
- [var sunElevation: Float](./sunelevation.md)
  The sun’s position in the simulated sky.
- [var upperAtmosphereScattering: Float](./upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundAlbedo: Float](./groundalbedo.md)
  A factor that influences the clarity of the simulated sky.
- [var groundColor: CGColor?](./groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](./horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/turbidity)*