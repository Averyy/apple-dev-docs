# seed

**Framework**: Core Animation  
**Kind**: property

Specifies the seed used to initialize the random number generator.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var seed: UInt32 { get set }
```

#### Discussion

Each layer has its own random number generator state. Emitter cell properties that are defined as a mean and a range, such as a cell’s `speed`, the value of the properties are uniformly distributed in the interval [M - R/2, M + R/2].

## See Also

- [var scale: Float](caemitterlayer/scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
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
- [var preservesDepth: Bool](caemitterlayer/preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/seed)*