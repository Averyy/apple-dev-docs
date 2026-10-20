# CATransitionType

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
struct CATransitionType
```

```c
typedef NSString * CATransitionType;
```

## Topics

### Initializers
- [init(rawValue: String)](./catransitiontype/init%28rawvalue%29.md)
### Type Properties
- [static let fade: CATransitionType](./catransitiontype/fade.md)
  The layer’s content fades as it becomes visible or hidden.
- [static let moveIn: CATransitionType](./catransitiontype/movein.md)
  The layer’s content slides into place over any existing content.
- [static let push: CATransitionType](./catransitiontype/push.md)
  The layer’s content pushes any existing content as it slides into place.
- [static let reveal: CATransitionType](./catransitiontype/reveal.md)
  The layer’s content is revealed gradually in the direction specified by the transition subtype.

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
- [struct CAShapeLayerFillRule](./cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](./cashapelayerlinecap.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransitiontype)*