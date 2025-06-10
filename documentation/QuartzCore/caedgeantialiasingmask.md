# CAEdgeAntialiasingMask

**Framework**: Core Animation  
**Kind**: struct

This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
struct CAEdgeAntialiasingMask
```

## Topics

### Constants
- [init(rawValue: UInt32)](caedgeantialiasingmask/init(rawvalue:).md)
- [static var layerLeftEdge: CAEdgeAntialiasingMask](caedgeantialiasingmask/layerleftedge.md)
- [static var layerRightEdge: CAEdgeAntialiasingMask](caedgeantialiasingmask/layerrightedge.md)
- [static var layerBottomEdge: CAEdgeAntialiasingMask](caedgeantialiasingmask/layerbottomedge.md)
- [static var layerTopEdge: CAEdgeAntialiasingMask](caedgeantialiasingmask/layertopedge.md)

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

- [struct CAAutoresizingMask](caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).
- [struct CATransform3D](catransform3d.md)
  The standard transform matrix used throughout Core Animation.
- [CALayer.DynamicRange](calayer/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caedgeantialiasingmask)*