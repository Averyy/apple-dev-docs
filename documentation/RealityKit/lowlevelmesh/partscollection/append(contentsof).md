# append(contentsOf:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Adds the elements of a sequence or collection to the end of this collection.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
mutating func append<S>(contentsOf newElements: S) where S : Sequence, S.Element == LowLevelMesh.Part
```

## Parameters

- `newElements`: The elements to append to the collection.

## See Also

### Updating collection contents
- [func append(LowLevelMesh.PartsCollection.Element)](./append%28_%29.md)
  Adds an element to the end of the collection.
- [func replaceAll<S>(S)](./replaceall%28_%29.md)
  Replaces all mesh parts in this collection with those from the new sequence.
- [func removeAll()](./removeall%28%29.md)
  Removes all mesh parts from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection/append(contentsof:))*