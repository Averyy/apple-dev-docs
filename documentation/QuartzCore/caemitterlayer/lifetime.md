# lifetime

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var lifetime: Float { get set }
```

```objc
@property float lifetime;
```

## Discussion

Default value is `1.0`.

By setting an emitter’s [`lifetime`](./lifetime.md) to `0`, you effectively stop particle emission: all new particles created have their [`lifetime`](../caemittercell/lifetime.md) set to `0` and are never rendered.

## See Also

### Emitter Cell Attribute Multipliers
- [var scale: Float](./scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
- [var seed: UInt32](./seed.md)
  Specifies the seed used to initialize the random number generator.
- [var spin: Float](./spin.md)
  Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [var velocity: Float](./velocity.md)
  Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [var birthRate: Float](./birthrate.md)
  Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [var emitterMode: CAEmitterLayerEmitterMode](./emittermode.md)
  Specifies the emitter mode.
- [var preservesDepth: Bool](./preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/lifetime)*