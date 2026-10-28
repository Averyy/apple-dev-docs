# sensor

**Framework**: RealityKit  
**Kind**: property  
**Role**: Type Property

A collision filter for an entity that collides with everything.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
static let sensor: CollisionFilter
```

## Discussion

The sensor collision filter is typically used by rays in ray casts, shapes in convex shape casts, and trigger volumes. It corresponds to a [`group`](./group.md) and [`mask`](./mask.md) both set to [`all`](../collisiongroup/all.md).

## See Also

### Creating a collision filter
- [init(group: CollisionGroup, mask: CollisionGroup)](./init%28group,mask%29.md)
  Creates a collision filter.
- [static let `default`: CollisionFilter](./default.md)
  The default collision filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter/sensor)*