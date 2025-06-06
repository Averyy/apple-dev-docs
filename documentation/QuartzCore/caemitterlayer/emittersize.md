# emitterSize

**Framework**: Core Animation  
**Kind**: property

Determines the size of the particle emitter shape. Animatable.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterSize: CGSize { get set }
```

#### Discussion

How the emitter size is applied depends on the emitter shape. See [`Emitter Shape`](emitter-shape.md) for details. Depending on the value of [`emitterShape`](caemitterlayer/emittershape.md), this value may be ignored.

Default is `0.0`.

## See Also

- [var renderMode: CAEmitterLayerRenderMode](caemitterlayer/rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](caemitterlayer/emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](caemitterlayer/emittershape.md)
  Specifies the emitter shape.
- [var emitterZPosition: CGFloat](caemitterlayer/emitterzposition.md)
  Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [var emitterDepth: CGFloat](caemitterlayer/emitterdepth.md)
  Determines the depth of the emitter shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittersize)*