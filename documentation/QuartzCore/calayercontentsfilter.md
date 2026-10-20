# CALayerContentsFilter

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
struct CALayerContentsFilter
```

```c
typedef NSString * CALayerContentsFilter;
```

## Topics

### Initializers
- [init(rawValue: String)](./calayercontentsfilter/init%28rawvalue%29.md)
### Type Properties
- [static let linear: CALayerContentsFilter](./calayercontentsfilter/linear.md)
  Linear interpolation filter.
- [static let nearest: CALayerContentsFilter](./calayercontentsfilter/nearest.md)
  Nearest neighbor interpolation filter.
- [static let trilinear: CALayerContentsFilter](./calayercontentsfilter/trilinear.md)
  Trilinear minification filter. Enables mipmap generation. Some renderers may ignore this, or impose additional restrictions, such as source images requiring power-of-two dimensions.

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

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayercontentsfilter)*