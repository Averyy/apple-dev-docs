# Scaling Filters

**Framework**: Core Animation

These constants specify the scaling filters used by [`magnificationFilter`](calayer/magnificationfilter.md) and [`minificationFilter`](calayer/minificationfilter.md).

## Topics

### Constants
- [static let linear: CALayerContentsFilter](calayercontentsfilter/linear.md)
  Linear interpolation filter.
- [static let nearest: CALayerContentsFilter](calayercontentsfilter/nearest.md)
  Nearest neighbor interpolation filter.
- [static let trilinear: CALayerContentsFilter](calayercontentsfilter/trilinear.md)
  Trilinear minification filter. Enables mipmap generation. Some renderers may ignore this, or impose additional restrictions, such as source images requiring power-of-two dimensions.

## See Also

- [struct CAAutoresizingMask](caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](calayer/autoresizingmask.md) property.
- [Action Identifiers](action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](calayer/action(forkey:).md), [`add(_:forKey:)`](calayer/add(_:forkey:).md), [`defaultAction(forKey:)`](calayer/defaultaction(forkey:).md), [`removeAnimation(forKey:)`](calayer/removeanimation(forkey:).md), Layer Filters, and the [`CAAction`](caaction.md) protocol method [`run(forKey:object:arguments:)`](caaction/run(forkey:object:arguments:).md).
- [struct CAEdgeAntialiasingMask](caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](calayer/edgeantialiasingmask.md) property.
- [Identity Transform](identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [struct CATransform3D](catransform3d.md)
  The standard transform matrix used throughout Core Animation.
- [CALayer.DynamicRange](calayer/dynamicrange.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/scaling-filters)*