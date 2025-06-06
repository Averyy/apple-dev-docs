# birthRate

**Framework**: Core Animation  
**Kind**: property

Defines a multiplier that is applied to the cell-defined birth rate. Animatable

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var birthRate: Float { get set }
```

#### Discussion

The birth rate of each cell is multiplied by this number to give the actual number of particles created every second. Default value is `1.0`.

## See Also

- [var scale: Float](caemitterlayer/scale.md)
  Defines a multiplier applied to the cell-defined particle scale.
- [var seed: UInt32](caemitterlayer/seed.md)
  Specifies the seed used to initialize the random number generator.
- [var spin: Float](caemitterlayer/spin.md)
  Defines a multiplier applied to the cell-defined particle spin. Animatable.
- [var velocity: Float](caemitterlayer/velocity.md)
  Defines a multiplier applied to the cell-defined particle velocity. Animatable.
- [var emitterMode: CAEmitterLayerEmitterMode](caemitterlayer/emittermode.md)
  Specifies the emitter mode.
- [var lifetime: Float](caemitterlayer/lifetime.md)
  Defines a multiplier applied to the cell-defined lifetime range when particles are created. Animatable.
- [var preservesDepth: Bool](caemitterlayer/preservesdepth.md)
  Defines whether the layer flattens the particles into its plane.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/birthrate)*