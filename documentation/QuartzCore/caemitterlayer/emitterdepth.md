# emitterDepth

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Determines the depth of the emitter shape.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var emitterDepth: CGFloat { get set }
```

```objc
@property CGFloat emitterDepth;
```

## Discussion

How the emitter depth is applied depends on the emitter shape. See [Emitter Shape](../emitter-shape.md) for details. Depending on the value of [`emitterShape`](./emittershape.md), this value may be ignored.

Default is `0.0`.

## See Also

### Emitter Geometry
- [var renderMode: CAEmitterLayerRenderMode](./rendermode.md)
  Defines how particle cells are rendered into the layer.
- [var emitterPosition: CGPoint](./emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](./emittershape.md)
  Specifies the emitter shape.
- [var emitterZPosition: CGFloat](./emitterzposition.md)
  Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [var emitterSize: CGSize](./emittersize.md)
  Determines the size of the particle emitter shape. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/emitterdepth)*