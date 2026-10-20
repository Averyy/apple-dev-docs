# CAAutoresizingMask

**Framework**: Core Animation  
**Kind**: struct  
**Role**: Structure

These constants are used by the [`autoresizingMask`](./calayer/autoresizingmask.md) property.

**Availability**:
- Mac Catalyst 13.1+
- macOS

## Declaration

```swift
struct CAAutoresizingMask
```

```c
enum CAAutoresizingMask : unsigned int;
```

## Topics

### Constants
- [init(rawValue: UInt32)](./caautoresizingmask/init%28rawvalue%29.md)
- [static var layerMinXMargin: CAAutoresizingMask](./caautoresizingmask/layerminxmargin.md)
  The left margin between the receiver and its superview is flexible.
- [static var layerWidthSizable: CAAutoresizingMask](./caautoresizingmask/layerwidthsizable.md)
  The receiver’s width is flexible.
- [static var layerMaxXMargin: CAAutoresizingMask](./caautoresizingmask/layermaxxmargin.md)
  The right margin between the receiver and its superview is flexible.
- [static var layerMinYMargin: CAAutoresizingMask](./caautoresizingmask/layerminymargin.md)
  The bottom margin between the receiver and its superview is flexible.
- [static var layerHeightSizable: CAAutoresizingMask](./caautoresizingmask/layerheightsizable.md)
  The receiver’s height is flexible.
- [static var layerMaxYMargin: CAAutoresizingMask](./caautoresizingmask/layermaxymargin.md)
  The top margin between the receiver and its superview is flexible.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Constants
- [Action Identifiers](./action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](./calayer/action%28forkey%29.md), [`add(_:forKey:)`](./calayer/add%28_,forkey%29.md), [`defaultAction(forKey:)`](./calayer/defaultaction%28forkey%29.md), [`removeAnimation(forKey:)`](./calayer/removeanimation%28forkey%29.md), Layer Filters, and the [`CAAction`](./caaction.md) protocol method [`run(forKey:object:arguments:)`](./caaction/run%28forkey,object,arguments%29.md).
- [struct CAEdgeAntialiasingMask](./caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](./calayer/edgeantialiasingmask.md) property.
- [Identity Transform](./identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](./scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](./calayer/magnificationfilter.md) and [`minificationFilter`](./calayer/minificationfilter.md).
- [struct CATransform3D](./catransform3d.md)
  The standard transform matrix used throughout Core Animation.
- [CALayer.DynamicRange](./calayer/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/caautoresizingmask)*