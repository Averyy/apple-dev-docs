# remove(_:)

**Framework**: Realitykit  
**Kind**: method

Removes the entity from the collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
mutating func remove(_ child: Entity)
```

#### Discussion

> **Note**: This operation can invalidate the index order of any remaining entities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/entitycollection/remove(_:))*