# CAAnimationCalculationMode

**Framework**: Core Animation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAAnimationCalculationMode
```

```c
typedef NSString * CAAnimationCalculationMode;
```

## Topics

### Initializers
- [init(rawValue: String)](./caanimationcalculationmode/init%28rawvalue%29.md)
### Type Properties
- [static let cubic: CAAnimationCalculationMode](./caanimationcalculationmode/cubic.md)
  Smooth spline calculation between keyframe values.
- [static let cubicPaced: CAAnimationCalculationMode](./caanimationcalculationmode/cubicpaced.md)
  Cubic keyframe values are interpolated to produce an even pace throughout the animation.
- [static let discrete: CAAnimationCalculationMode](./caanimationcalculationmode/discrete.md)
  Each keyframe value is used in turn, no interpolated values are calculated.
- [static let linear: CAAnimationCalculationMode](./caanimationcalculationmode/linear.md)
  Simple linear calculation between keyframe values.
- [static let paced: CAAnimationCalculationMode](./caanimationcalculationmode/paced.md)
  Linear keyframe values are interpolated to produce an even pace throughout the animation.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Types
- [struct CAAnimationRotationMode](./caanimationrotationmode.md)
- [struct CAEmitterLayerEmitterMode](./caemitterlayeremittermode.md)
- [struct CAEmitterLayerEmitterShape](./caemitterlayeremittershape.md)
- [struct CAEmitterLayerRenderMode](./caemitterlayerrendermode.md)
- [struct CAGradientLayerType](./cagradientlayertype.md)
- [struct CALayerContentsFilter](./calayercontentsfilter.md)
- [struct CALayerContentsFormat](./calayercontentsformat.md)
- [struct CALayerContentsGravity](./calayercontentsgravity.md)
- [struct CALayerCornerCurve](./calayercornercurve.md)
- [struct CAMediaTimingFillMode](./camediatimingfillmode.md)
- [struct CAMediaTimingFunctionName](./camediatimingfunctionname.md)
- [struct CAScrollLayerScrollMode](./cascrolllayerscrollmode.md)
- [struct CAShapeLayerFillRule](./cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](./cashapelayerlinecap.md)
- [struct CAShapeLayerLineJoin](./cashapelayerlinejoin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caanimationcalculationmode)*