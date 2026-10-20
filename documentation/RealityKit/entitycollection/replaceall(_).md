# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Replaces all entities in this collection with those from the given sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
mutating func replaceAll<S>(_ entities: S) where S : Sequence, S.Element : Entity
```

#### Discussion

> **Note**: This operation might not maintain the new entities’ index order.

## Parameters

- `entities`: The sequence of entities that will replace the collection’s current contents.

## Default Implementations

### EntityCollection Implementations
- [func replaceAll<S>(S)](./replaceall%28_%29-91uho.md)
  Replaces all entities in this collection with those from the given sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entitycollection/replaceall(_:))*