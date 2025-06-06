# replaceAll(_:)

**Framework**: Realitykit  
**Kind**: method

Replaces all entities in this collection with those from the given sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
mutating func replaceAll<S>(_ children: S) where S : Sequence, S.Element : Entity
```

#### Discussion

> **Note**: This operation might not maintain the new entities’ index order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityrenderer/entitycollection/replaceall(_:))*