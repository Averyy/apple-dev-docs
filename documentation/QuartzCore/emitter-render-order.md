# Emitter Render Order

**Framework**: Core Animation

These constants specify the order that emitter cells are composited. They are used by the [`renderMode`](caemitterlayer/rendermode.md) property.

## Topics

### Constants
- [static let unordered: CAEmitterLayerRenderMode](caemitterlayerrendermode/unordered.md)
  Particles are rendered unordered. This mode uses source-over compositing.
- [static let oldestFirst: CAEmitterLayerRenderMode](caemitterlayerrendermode/oldestfirst.md)
  Particles are rendered oldest first. This mode uses source-over compositing.
- [static let oldestLast: CAEmitterLayerRenderMode](caemitterlayerrendermode/oldestlast.md)
  Particles are rendered oldest last. This mode uses source-over compositing.
- [static let backToFront: CAEmitterLayerRenderMode](caemitterlayerrendermode/backtofront.md)
  Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [static let additive: CAEmitterLayerRenderMode](caemitterlayerrendermode/additive.md)
  The particles are rendered using source-additive compositing.

## See Also

- [Emitter Shape](emitter-shape.md)
  The emission shape is a one, two or three dimensional shape that defines where the emitted particles originate. The shapes are defined by a subset of [`emitterPosition`](caemitterlayer/emitterposition.md), [`emitterZPosition`](caemitterlayer/emitterzposition.md), [`emitterSize`](caemitterlayer/emittersize.md) and [`emitterDepth`](caemitterlayer/emitterdepth.md) properties.
- [Emitter Modes](emitter-modes.md)
  These constants specify the possible emitter modes. They are used by the [`emitterMode`](caemitterlayer/emittermode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/emitter-render-order)*