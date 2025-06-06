# append(contentsOf:)

**Framework**: RealityKit  
**Kind**: method

Adds the elements of a sequence or collection to the end of this collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
mutating func append<S>(contentsOf newElements: S) where S : Sequence, S.Element == LowLevelMesh.Part
```

## Parameters

- `newElements`: The elements to append to the collection.

## See Also

- [func append(LowLevelMesh.PartsCollection.Element)](lowlevelmesh/partscollection/append(_:).md)
  Adds an element to the end of the collection.
- [func replaceAll<S>(S)](lowlevelmesh/partscollection/replaceall(_:).md)
  Replaces all mesh parts in this collection with those from the new sequence.
- [func removeAll()](lowlevelmesh/partscollection/removeall.md)
  Removes all mesh parts from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection/append(contentsof:))*