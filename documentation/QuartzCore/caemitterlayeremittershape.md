# CAEmitterLayerEmitterShape

**Framework**: Core Animation  
**Kind**: struct

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAEmitterLayerEmitterShape
```

## Topics

### Initializers
- [init(rawValue: String)](caemitterlayeremittershape/init(rawvalue:).md)
### Type Properties
- [static let circle: CAEmitterLayerEmitterShape](caemitterlayeremittershape/circle.md)
  Particles are emitted from a circle centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.
- [static let cuboid: CAEmitterLayerEmitterShape](caemitterlayeremittershape/cuboid.md)
  Particles are emitted from a cuboid (3D rectangle) with opposite corners: [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition - emitterDepth/2], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition+emitterDepth/2].
- [static let line: CAEmitterLayerEmitterShape](caemitterlayeremittershape/line.md)
  Particles are emitted along a line from (`emitterPosition.x - emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`) to (`emitterPosition.x + emitterSize.width/2`, `emitterPosition.y`, `emitterZPosition`).
- [static let point: CAEmitterLayerEmitterShape](caemitterlayeremittershape/point.md)
  Particles are emitted from a single point at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`)
- [static let rectangle: CAEmitterLayerEmitterShape](caemitterlayeremittershape/rectangle.md)
  Particles are emitted from a rectangle with opposite corners [emitterPosition.x - emitterSize.width/2, emitterPosition.y - emitterSize.height/2, emitterZPosition], [emitterPosition.x + emitterSize.width/2, emitterPosition.y + emitterSize.height/2, emitterZPosition].
- [static let sphere: CAEmitterLayerEmitterShape](caemitterlayeremittershape/sphere.md)
  Particles are emitted from a sphere centered at (`emitterPosition.x`, `emitterPosition.y`, `emitterZPosition`) of radius `emitterSize.width`.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct CAAnimationCalculationMode](caanimationcalculationmode.md)
- [struct CAAnimationRotationMode](caanimationrotationmode.md)
- [struct CAEmitterLayerEmitterMode](caemitterlayeremittermode.md)
- [struct CAEmitterLayerRenderMode](caemitterlayerrendermode.md)
- [struct CAGradientLayerType](cagradientlayertype.md)
- [struct CALayerContentsFilter](calayercontentsfilter.md)
- [struct CALayerContentsFormat](calayercontentsformat.md)
- [struct CALayerContentsGravity](calayercontentsgravity.md)
- [struct CALayerCornerCurve](calayercornercurve.md)
- [struct CAMediaTimingFillMode](camediatimingfillmode.md)
- [struct CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [struct CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [struct CAShapeLayerFillRule](cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](cashapelayerlinecap.md)
- [struct CAShapeLayerLineJoin](cashapelayerlinejoin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayeremittershape)*