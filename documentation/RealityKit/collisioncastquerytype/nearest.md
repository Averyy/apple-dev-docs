# CollisionCastQueryType.nearest

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

Report the closest hit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
case nearest
```

#### Discussion

If you only want to test if a hit occurs and don’t care about which hit out of multiple possible hits is returned, use [`CollisionCastQueryType.any`](./any.md) instead because it typically executes faster.

## See Also

### Collision cast queries
- [CollisionCastQueryType.all](./all.md)
  Report all hits sorted in ascending order by distance from the cast origin.
- [CollisionCastQueryType.any](./any.md)
  Report one hit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/collisioncastquerytype/nearest)*