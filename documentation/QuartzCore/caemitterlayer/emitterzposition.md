# emitterZPosition

**Framework**: Core Animation  
**Kind**: property

Specifies the center of the particle emitter shape along the z-axis. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterZPosition: CGFloat { get set }
```

#### Discussion

See [`Emitter Shape`](emitter-shape.md) for details of how the emitterZPosition relates to the possible emitter shapes.

Default is `0.0`.

## See Also

- [var renderMode: CAEmitterLayerRenderMode](caemitterlayer/rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](caemitterlayer/emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](caemitterlayer/emittershape.md)
  Specifies the emitter shape.
- [var emitterDepth: CGFloat](caemitterlayer/emitterdepth.md)
  Determines the depth of the emitter shape.
- [var emitterSize: CGSize](caemitterlayer/emittersize.md)
  Determines the size of the particle emitter shape. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emitterzposition)*