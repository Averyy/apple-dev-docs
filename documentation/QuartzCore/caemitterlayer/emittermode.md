# emitterMode

**Framework**: Core Animation  
**Kind**: property

Specifies the emitter mode.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterMode: CAEmitterLayerEmitterMode { get set }
```

#### Discussion

The possible values for emitterMode are shown in [`Emitter Modes`](emitter-modes.md). The default value is [`volume`](caemitterlayeremittermode/volume.md).

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
- [var lifetime: Float](caemitterlayer/lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [var preservesDepth: Bool](caemitterlayer/preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittermode)*