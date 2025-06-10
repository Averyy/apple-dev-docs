# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method  
**Required**: Yes

Replaces all entities in this collection with those from the given sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

## Declaration

```swift
mutating func replaceAll<S>(_ entities: S) where S : Sequence, S.Element : Entity
```

#### Discussion

> **Note**: This operation might not maintain the new entities’ index order.

## Parameters

- `entities`: The sequence of entities that will replace   the collection’s current contents.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection/replaceall(_:))*