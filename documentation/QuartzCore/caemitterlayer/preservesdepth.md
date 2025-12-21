# preservesDepth

**Framework**: Core Animation  
**Kind**: property

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

#### Discussion

If [`true`](https://developer.apple.com/documentation/Swift/true), the layer renders its particles as if they directly inhabit the three-dimensional coordinate space of the layer’s superlayer. When enabled, the effect of the layer’s `filters`, `backgroundFilters`, and shadow related properties is undefined.

Default is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var scale: Float](caemitterlayer/scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
- [var seed: UInt32](caemitterlayer/seed.md)
  Specifies the seed used to initialize the random number generator.
- [var spin: Float](caemitterlayer/spin.md)
  Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [var velocity: Float](caemitterlayer/velocity.md)
  Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [var birthRate: Float](caemitterlayer/birthrate.md)
  Defines a multiplier that is applied to the cell-defined birth rate. Animatable
- [var emitterMode: CAEmitterLayerEmitterMode](caemitterlayer/emittermode.md)
  Specifies the emitter mode.
- [var lifetime: Float](caemitterlayer/lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/preservesdepth)*