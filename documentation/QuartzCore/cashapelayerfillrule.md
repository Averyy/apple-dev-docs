# CAShapeLayerFillRule

**Framework**: Core Animation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAShapeLayerFillRule
```

```c
typedef NSString * CAShapeLayerFillRule;
```

## Topics

### Initializers
- [init(rawValue: String)](./cashapelayerfillrule/init%28rawvalue%29.md)
### Type Properties
- [static let evenOdd: CAShapeLayerFillRule](./cashapelayerfillrule/evenodd.md)
  Specifies the even-odd winding rule. Count the total number of path crossings. If the number of crossings is even, the point is outside the path. If the number of crossings is odd, the point is inside the path and the region containing it should be filled.
- [static let nonZero: CAShapeLayerFillRule](./cashapelayerfillrule/nonzero.md)
  Specifies the non-zero winding rule. Count each left-to-right path as +1 and each right-to-left path as -1. If the sum of all crossings is 0, the point is outside the path. If the sum is nonzero, the point is inside the path and the region containing it is filled.

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
- [struct CAMediaTimingFunctionName](./camediatimingfunctionname.md)
- [struct CAScrollLayerScrollMode](./cascrolllayerscrollmode.md)
- [struct CAShapeLayerLineCap](./cashapelayerlinecap.md)
- [struct CAShapeLayerLineJoin](./cashapelayerlinejoin.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cashapelayerfillrule)*