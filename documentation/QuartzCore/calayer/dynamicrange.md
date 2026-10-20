# CALayer.DynamicRange

**Framework**: Core Animation  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DynamicRange
```

```c
typedef NSString * CADynamicRange;
```

## Topics

### Constants
- [static let automatic: CALayer.DynamicRange](./dynamicrange/automatic.md)
- [static let standard: CALayer.DynamicRange](./dynamicrange/standard.md)
- [static let constrainedHigh: CALayer.DynamicRange](./dynamicrange/constrainedhigh.md)
- [static let high: CALayer.DynamicRange](./dynamicrange/high.md)
### Initializers
- [init(rawValue: String)](./dynamicrange/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Constants
- [struct CAAutoresizingMask](../caautoresizingmask.md)
  These constants are used by the [`autoresizingMask`](./autoresizingmask.md) property.
- [Action Identifiers](../action-identifiers.md)
  These constants are the predefined action identifiers used by [`action(forKey:)`](./action%28forkey%29.md), [`add(_:forKey:)`](./add%28_,forkey%29.md), [`defaultAction(forKey:)`](./defaultaction%28forkey%29.md), [`removeAnimation(forKey:)`](./removeanimation%28forkey%29.md), Layer Filters, and the [`CAAction`](../caaction.md) protocol method [`run(forKey:object:arguments:)`](../caaction/run%28forkey,object,arguments%29.md).
- [struct CAEdgeAntialiasingMask](../caedgeantialiasingmask.md)
  This mask is used by the [`edgeAntialiasingMask`](./edgeantialiasingmask.md) property.
- [Identity Transform](../identity-transform.md)
  Defines the identity transform matrix used by Core Animation.
- [Scaling Filters](../scaling-filters.md)
  These constants specify the scaling filters used by [`magnificationFilter`](./magnificationfilter.md) and [`minificationFilter`](./minificationfilter.md).
- [struct CATransform3D](../catransform3d.md)
  The standard transform matrix used throughout Core Animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/dynamicrange)*