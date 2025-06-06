# append(contentsOf:)

**Framework**: Realitykit  
**Kind**: method

Adds the specified sequence of entities to the end of this collection, in order.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
mutating func append<S>(contentsOf sequence: S) where S : Sequence, S.Element : Entity
```

#### Discussion

> **Note**: This operation can invalidate the index order of any extant entities.

## Parameters

- `sequence`: The entities to add to the collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/realityviewentitycollection/append(contentsof:))*