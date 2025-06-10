# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces all mesh parts in this collection with those from the new sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
mutating func replaceAll<S>(_ newElements: S) where S : Sequence, S.Element == LowLevelMesh.Part
```

## Parameters

- `newElements`: The elements to replace the contents of the collection.

## See Also

- [func append(LowLevelMesh.PartsCollection.Element)](lowlevelmesh/partscollection/append(_:).md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](lowlevelmesh/partscollection/append(contentsof:).md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func removeAll()](lowlevelmesh/partscollection/removeall.md)
  Removes all mesh parts from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection/replaceall(_:))*