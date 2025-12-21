# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method

Removes all children from this entity and adds the specified list of entities as the new children.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency func replaceAll<S>(_ children: S) where S : Sequence, S.Element : Entity
```

## Parameters

- `children`: The list of the new children.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/childcollection/replaceall(_:))*