# Action Identifiers

**Framework**: Core Animation

These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).

## Topics

### Constants
- [let kCAOnOrderIn: String](kcaonorderin.md)
  The identifier that represents the action taken when a layer becomes visible, either as a result being inserted into the visible layer hierarchy or the layer is no longer set as hidden.
- [let kCAOnOrderOut: String](kcaonorderout.md)
  The identifier that represents the action taken when the layer is removed from the layer hierarchy or is hidden.
- [let kCATransition: String](kcatransition.md)
  The identifier that represents a transition animation.

## See Also

- [struct CAAutoresizingMask](caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.
- [struct CAEdgeAntialiasingMask](caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).
- [struct CATransform3D](catransform3d.md)
  The standard transform matrix used throughout Core Animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/action-identifiers)*