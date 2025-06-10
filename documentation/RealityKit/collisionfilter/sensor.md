# sensor

**Framework**: RealityKit  
**Kind**: property

A collision filter for an entity that collides with everything.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
static let sensor: CollisionFilter
```

#### Discussion

The sensor collision filter is typically used by rays in ray casts, shapes in convex shape casts, and trigger volumes. It corresponds to a [`group`](collisionfilter/group.md) and [`mask`](collisionfilter/mask.md) both set to [`all`](collisiongroup/all.md).

## See Also

- [init(group: CollisionGroup, mask: CollisionGroup)](collisionfilter/init(group:mask:).md)
  Creates a collision filter.
- [static let `default`: CollisionFilter](collisionfilter/default.md)
  The default collision filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisionfilter/sensor)*