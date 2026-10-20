# emitterZPosition

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property CGFloat emitterZPosition;
```

#### Discussion

See [Emitter Shape](../emitter-shape.md) for details of how the emitterZPosition relates to the possible emitter shapes.

Default is `0.0`.

## See Also

### Emitter Geometry
- [var renderMode: CAEmitterLayerRenderMode](./rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](./emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](./emittershape.md)
  Specifies the emitter shape.
- [var emitterDepth: CGFloat](./emitterdepth.md)
  Determines the depth of the emitter shape.
- [var emitterSize: CGSize](./emittersize.md)
  Determines the size of the particle emitter shape. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emitterzposition)*