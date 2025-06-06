# Emitter Shape

**Framework**: Core Animation

The emission shape is a one, two or three dimensional shape that defines where the emitted particles originate. The shapes are defined by a subset of [`emitterPosition`](caemitterlayer/emitterposition.md), [`emitterZPosition`](caemitterlayer/emitterzposition.md), [`emitterSize`](caemitterlayer/emittersize.md) and [`emitterDepth`](caemitterlayer/emitterdepth.md) properties.

## Topics

### Constants
- [static let point: CAEmitterLayerEmitterShape](caemitterlayeremittershape/point.md)
  Particles are emitted from a single point at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`)
- [static let line: CAEmitterLayerEmitterShape](caemitterlayeremittershape/line.md)
  Particles are emitted along a line from (`emitterPosition.x - emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`) to (`emitterPosition.x + emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`).
- [static let rectangle: CAEmitterLayerEmitterShape](caemitterlayeremittershape/rectangle.md)
  Particles are emitted from a rectangle with opposite corners [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition].
- [static let cuboid: CAEmitterLayerEmitterShape](caemitterlayeremittershape/cuboid.md)
  Particles are emitted from a cuboid (3D rectangle) with opposite corners: [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition - emitterDepth/2], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition+emitterDepth/2].
- [static let circle: CAEmitterLayerEmitterShape](caemitterlayeremittershape/circle.md)
  Particles are emitted from a circle centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
- [static let sphere: CAEmitterLayerEmitterShape](caemitterlayeremittershape/sphere.md)
  Particles are emitted from a sphere centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.

## See Also

- [Emitter Modes](emitter-modes.md)
  These constants specify the possible emitter modes. They are used by the [`emitterMode`](caemitterlayer/emittermode.md) property.
- [Emitter Render Order](emitter-render-order.md)
  These constants specify the order that emitter cells are composited. They are used by the [`renderMode`](caemitterlayer/rendermode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/emitter-shape)*