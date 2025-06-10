# CollisionCastQueryType.any

**Framework**: RealityKit  
**Kind**: case

Report one hit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case any
```

#### Discussion

This query type typically executes fastest, but doesn’t guarantee anything about which hit it returns. If you need the hit closest to the origin of the cast, use [`CollisionCastQueryType.nearest`](collisioncastquerytype/nearest.md) instead.

## See Also

- [CollisionCastQueryType.nearest](collisioncastquerytype/nearest.md)
  Report the closest hit.
- [CollisionCastQueryType.all](collisioncastquerytype/all.md)
  Report all hits sorted in ascending order by distance from the cast origin.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncastquerytype/any)*