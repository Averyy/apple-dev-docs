# rectangle

**Framework**: Core Animation  
**Kind**: property

Particles are emitted from a rectangle with opposite corners [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition].

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
static let rectangle: CAEmitterLayerEmitterShape
```

## See Also

- [static let point: CAEmitterLayerEmitterShape](caemitterlayeremittershape/point.md)
  Particles are emitted from a single point at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`)
- [static let line: CAEmitterLayerEmitterShape](caemitterlayeremittershape/line.md)
  Particles are emitted along a line from (`emitterPosition.x - emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`) to (`emitterPosition.x + emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`).
- [static let cuboid: CAEmitterLayerEmitterShape](caemitterlayeremittershape/cuboid.md)
  Particles are emitted from a cuboid (3D rectangle) with opposite corners: [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition - emitterDepth/2], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition+emitterDepth/2].
- [static let circle: CAEmitterLayerEmitterShape](caemitterlayeremittershape/circle.md)
  Particles are emitted from a circle centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
- [static let sphere: CAEmitterLayerEmitterShape](caemitterlayeremittershape/sphere.md)
  Particles are emitted from a sphere centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape/rectangle)*