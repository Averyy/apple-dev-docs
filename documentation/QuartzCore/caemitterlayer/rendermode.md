# renderMode

**Framework**: Core Animation  
**Kind**: property  
**Role**: Instance Property

Defines how particle cells are rendered into the layer.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderMode: CAEmitterLayerRenderMode { get set }
```

```objc
@property (copy) CAEmitterLayerRenderMode renderMode;
```

#### Discussion

The possible values for render modes are shown in [Emitter Modes](../emitter-modes.md). The default value is [`unordered`](../caemitterlayerrendermode/unordered.md).

## See Also

### Emitter Geometry
- [var emitterPosition: CGPoint](./emitterposition.md)
  The position of the center of the particle emitter. Animatable.
- [var emitterShape: CAEmitterLayerEmitterShape](./emittershape.md)
  Specifies the emitter shape.
- [var emitterZPosition: CGFloat](./emitterzposition.md)
  Specifies the center of the particle emitter shape along the z-axis. Animatable.
- [var emitterDepth: CGFloat](./emitterdepth.md)
  Determines the depth of the emitter shape.
- [var emitterSize: CGSize](./emittersize.md)
  Determines the size of the particle emitter shape. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayer/rendermode)*