# CAEmitterLayerRenderMode

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
struct CAEmitterLayerRenderMode
```

## Topics

### Initializers
- [init(rawValue: String)](caemitterlayerrendermode/init(rawvalue:).md)
### Type Properties
- [static let additive: CAEmitterLayerRenderMode](caemitterlayerrendermode/additive.md)
  The particles are rendered using source-additive compositing.
- [static let backToFront: CAEmitterLayerRenderMode](caemitterlayerrendermode/backtofront.md)
  Particles are rendered from back to front, sorted by z-position. This mode uses source-over compositing.
- [static let oldestFirst: CAEmitterLayerRenderMode](caemitterlayerrendermode/oldestfirst.md)
  Particles are rendered oldest first. This mode uses source-over compositing.
- [static let oldestLast: CAEmitterLayerRenderMode](caemitterlayerrendermode/oldestlast.md)
  Particles are rendered oldest last. This mode uses source-over compositing.
- [static let unordered: CAEmitterLayerRenderMode](caemitterlayerrendermode/unordered.md)
  Particles are rendered unordered. This mode uses source-over compositing.

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
- [struct CAEmitterLayerEmitterShape](caemitterlayeremittershape.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caemitterlayerrendermode)*