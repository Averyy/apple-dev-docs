# spin

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines a multiplier applied to the cell-defined particle spin. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var spin: Float { get set }
```

```objc
@property float spin;
```

#### Discussion

Default value is `1.0`.

## See Also

### Emitter Cell Attribute Multipliers
- [var scale: Float](./scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
- [var seed: UInt32](./seed.md)
  Specifies the seed used to initialize the random number generator.
- [var velocity: Float](./velocity.md)
  Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [var birthRate: Float](./birthrate.md)
  Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [var emitterMode: CAEmitterLayerEmitterMode](./emittermode.md)
  Specifies the emitter mode.
- [var lifetime: Float](./lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [var preservesDepth: Bool](./preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/spin)*