# replaceAll(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Replaces all mesh parts in this collection with those from the new sequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
mutating func replaceAll<S>(_ newElements: S) where S : Sequence, S.Element == LowLevelMesh.Part
```

## Parameters

- `newElements`: The elements to replace the contents of the collection.

## See Also

### Updating collection contents
- [func append(LowLevelMesh.PartsCollection.Element)](./append%28_%29.md)
  Adds an element to the end of the collection.
- [func append<S>(contentsOf: S)](./append%28contentsof%29.md)
  Adds the elements of a sequence or collection to the end of this collection.
- [func removeAll()](./removeall%28%29.md)
  Removes all mesh parts from this collection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowlevelmesh/partscollection/replaceall(_:))*