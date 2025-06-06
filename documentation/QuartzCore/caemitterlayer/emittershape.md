# emitterShape

**Framework**: Core Animation  
**Kind**: property

Specifies the emitter shape.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterShape: CAEmitterLayerEmitterShape { get set }
```

#### Discussion

The possible values for emitterMode are shown in [`Emitter Shape`](emitter-shape.md). The default value is [`point`](caemitterlayeremittershape/point.md).

## See Also

- [var renderMode: CAEmitterLayerRenderMode](caemitterlayer/rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](caemitterlayer/emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterZPosition: CGFloat](caemitterlayer/emitterzposition.md)
  Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [var emitterDepth: CGFloat](caemitterlayer/emitterdepth.md)
  Determines the depth of the emitter shape.
- [var emitterSize: CGSize](caemitterlayer/emittersize.md)
  Determines the size of the particle emitter shape. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emittershape)*