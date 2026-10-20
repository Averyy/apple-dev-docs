# CAMediaTimingFunctionName

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
struct CAMediaTimingFunctionName
```

```c
typedef NSString * CAMediaTimingFunctionName;
```

## Topics

### Initializers
- [init(rawValue: String)](./camediatimingfunctionname/init%28rawvalue%29.md)
### Type Properties
- [static let `default`: CAMediaTimingFunctionName](./camediatimingfunctionname/default.md)
  The system default timing function. Use this function to ensure that the timing of your animations matches that of most system animations.
- [static let easeIn: CAMediaTimingFunctionName](./camediatimingfunctionname/easein.md)
  Ease-in pacing, which causes an animation to begin slowly and then speed up as it progresses.
- [static let easeInEaseOut: CAMediaTimingFunctionName](./camediatimingfunctionname/easeineaseout.md)
  Ease-in-ease-out pacing, which causes an animation to begin slowly, accelerate through the middle of its duration, and then slow again before completing.
- [static let easeOut: CAMediaTimingFunctionName](./camediatimingfunctionname/easeout.md)
  Ease-out pacing, which causes an animation to begin quickly and then slow as it progresses.
- [static let linear: CAMediaTimingFunctionName](./camediatimingfunctionname/linear.md)
  Linear pacing, which causes an animation to occur evenly over its duration.

## Relationships

### Conforms To
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Data Types
- [struct CAAnimationCalculationMode](./caanimationcalculationmode.md)
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
- [struct CAScrollLayerScrollMode](./cascrolllayerscrollmode.md)
- [struct CAShapeLayerFillRule](./cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](./cashapelayerlinecap.md)
- [struct CAShapeLayerLineJoin](./cashapelayerlinejoin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/camediatimingfunctionname)*