# CAAutoresizingMask

**Framework**: Core Animation  
**Kind**: struct

These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.

**Availability**:
- Mac Catalyst 13.1+
- macOS ?+

## Declaration

```swift
struct CAAutoresizingMask
```

## Topics

### Constants
- [init(rawValue: UInt32)](caautoresizingmask/init(rawvalue:).md)
- [static var layerMinXMargin: CAAutoresizingMask](caautoresizingmask/layerminxmargin.md)
  The left margin between the receiver and its superview is flexible.
- [static var layerWidthSizable: CAAutoresizingMask](caautoresizingmask/layerwidthsizable.md)
  The receiver’s width is flexible.
- [static var layerMaxXMargin: CAAutoresizingMask](caautoresizingmask/layermaxxmargin.md)
  The right margin between the receiver and its superview is flexible.
- [static var layerMinYMargin: CAAutoresizingMask](caautoresizingmask/layerminymargin.md)
  The bottom margin between the receiver and its superview is flexible.
- [static var layerHeightSizable: CAAutoresizingMask](caautoresizingmask/layerheightsizable.md)
  The receiver’s height is flexible.
- [static var layerMaxYMargin: CAAutoresizingMask](caautoresizingmask/layermaxymargin.md)
  The top margin between the receiver and its superview is flexible.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Action Identifiers](action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).
- [struct CAEdgeAntialiasingMask](caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).
- [struct CATransform3D](catransform3d.md)
  The standard transform matrix used throughout Core Animation.
- [CALayer.DynamicRange](calayer/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caautoresizingmask)*