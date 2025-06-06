# CAValueFunctionName

**Framework**: Core Animation  
**Kind**: struct

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAValueFunctionName
```

## Topics

### Initializers
- [init(rawValue: String)](cavaluefunctionname/init(rawvalue:).md)
### Type Properties
- [static let rotateX: CAValueFunctionName](cavaluefunctionname/rotatex.md)
  A value function that rotates by the input value, in radians, around the x-axis. This value function expects a single input value.
- [static let rotateY: CAValueFunctionName](cavaluefunctionname/rotatey.md)
  A value function that rotates by the input value, in radians, around the y-axis. This value function expects a single input value.
- [static let rotateZ: CAValueFunctionName](cavaluefunctionname/rotatez.md)
  A value function that rotates by the input value, in radians, around the z-axis. This value function expects a single input value.
- [static let scale: CAValueFunctionName](cavaluefunctionname/scale.md)
  A value function scales by the input value along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) scale values.
- [static let scaleX: CAValueFunctionName](cavaluefunctionname/scalex.md)
  A value function scales by the input value along the x-axis. Animations referencing this value transform function must provide a single animation value.
- [static let scaleY: CAValueFunctionName](cavaluefunctionname/scaley.md)
  A value function scales by the input value along the y-axis. Animations referencing this value function must provide a single animation value.
- [static let scaleZ: CAValueFunctionName](cavaluefunctionname/scalez.md)
  A value function that scales by the input value along the z-axis. Animations referencing this value function must provide a single animation value.
- [static let translate: CAValueFunctionName](cavaluefunctionname/translate.md)
  A value function that translates by the input values along all three axis. Animations using this value transform function must provide animation values in an `NSArray` of three `NSNumber` instances that specify the (x, y, z) translate values.
- [static let translateX: CAValueFunctionName](cavaluefunctionname/translatex.md)
  A value function translates by the input value along the x-axis. Animations referencing this value function must provide a single input value.
- [static let translateY: CAValueFunctionName](cavaluefunctionname/translatey.md)
  A value function translates by the input value along the y-axis. Animations referencing this value function must provide a single input value.
- [static let translateZ: CAValueFunctionName](cavaluefunctionname/translatez.md)
  A value function translates by the input value along the z-axis. Animations referencing this value function must provide a single input value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [struct CAMediaTimingFillMode](camediatimingfillmode.md)
- [struct CAMediaTimingFunctionName](camediatimingfunctionname.md)
- [struct CAScrollLayerScrollMode](cascrolllayerscrollmode.md)
- [struct CAShapeLayerFillRule](cashapelayerfillrule.md)
- [struct CAShapeLayerLineCap](cashapelayerlinecap.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cavaluefunctionname)*