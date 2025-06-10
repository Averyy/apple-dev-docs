# CAMediaTimingFillMode

**Framework**: Core Animation  
**Kind**: struct

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAMediaTimingFillMode
```

## Topics

### Initializers
- [init(rawValue: String)](camediatimingfillmode/init(rawvalue:).md)
### Type Properties
- [static let backwards: CAMediaTimingFillMode](camediatimingfillmode/backwards.md)
  The receiver clamps values before zero to zero when the animation is completed.
- [static let both: CAMediaTimingFillMode](camediatimingfillmode/both.md)
  The receiver clamps values at both ends of the object’s time space
- [static let forwards: CAMediaTimingFillMode](camediatimingfillmode/forwards.md)
  The receiver remains visible in its final state when the animation is completed.
- [static let removed: CAMediaTimingFillMode](camediatimingfillmode/removed.md)
  The receiver is removed from the presentation when the animation is completed.

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
- [struct CAEmitterLayerRenderMode](caemitterlayerrendermode.md)
- [struct CAGradientLayerType](cagradientlayertype.md)
- [struct CALayerContentsFilter](calayercontentsfilter.md)
- [struct CALayerContentsFormat](calayercontentsformat.md)
- [struct CALayerContentsGravity](calayercontentsgravity.md)
- [struct CALayerCornerCurve](calayercornercurve.md)
- [struct CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [struct CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [struct CAShapeLayerFillRule](cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](cashapelayerlinecap.md)
- [struct CAShapeLayerLineJoin](cashapelayerlinejoin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfillmode)*