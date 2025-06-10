# removeAll(where:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Removes all entities from this collection that satisfy the given predicate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
mutating func removeAll(where: (Entity) throws -> Bool) rethrows
```

#### Discussion

> **Note**: This operation can invalidate the index order of any remaining entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection/removeall(where:))*