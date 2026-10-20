# groundAlbedo

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

A factor that influences the clarity of the simulated sky.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var groundAlbedo: Float { get set }
```

```objc
@property (nonatomic, assign) float groundAlbedo;
```

#### Discussion

This value simulates the amount of light that bounces back up into the sky from the ground. A value of `0.0` produces a clear sky, and values closer to `10` reduce the contrast of the sky, producing a foggy effect.

## See Also

### Working with Sky Simulation Parameters
- [var turbidity: Float](./turbidity.md)
  The cloudiness or haziness of the simulated sky.
- [var sunElevation: Float](./sunelevation.md)
  The sun’s position in the simulated sky.
- [var upperAtmosphereScattering: Float](./upperatmospherescattering.md)
  A factor that influences the color of the simulated sky.
- [var groundColor: CGColor?](./groundcolor.md)
  The color of the simulated ground.
- [var horizonElevation: Float](./horizonelevation.md)
  The angle, in radians relative to center, below which to render the ground color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlskycubetexture/groundalbedo)*