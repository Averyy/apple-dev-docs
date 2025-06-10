# CollisionCastQueryType.nearest

**Framework**: RealityKit  
**Kind**: case

Report the closest hit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
case nearest
```

#### Discussion

If you only want to test if a hit occurs and don’t care about which hit out of multiple possible hits is returned, use [`CollisionCastQueryType.any`](collisioncastquerytype/any.md) instead because it typically executes faster.

## See Also

- [CollisionCastQueryType.all](collisioncastquerytype/all.md)
  Report all hits sorted in ascending order by distance from the cast origin.
- [CollisionCastQueryType.any](collisioncastquerytype/any.md)
  Report one hit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncastquerytype/nearest)*