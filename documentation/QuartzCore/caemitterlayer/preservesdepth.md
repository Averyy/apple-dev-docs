# preservesDepth

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines whether the layer flattens the particles into its plane.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var preservesDepth: Bool { get set }
```

```objc
@property BOOL preservesDepth;
```

#### Discussion

If [`true`](../../Swift/true.md), the layer renders its particles as if they directly inhabit the three-dimensional coordinate space of the layer’s superlayer. When enabled, the effect of the layer’s `filters`, `backgroundFilters`, and shadow related properties is undefined.

Default is [`false`](../../Swift/false.md).

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
- [var lifetime: Float](./lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/preservesdepth)*