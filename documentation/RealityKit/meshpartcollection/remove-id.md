# remove(id:)

**Framework**: RealityKit  
**Kind**: method

Remove a part by id.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
@discardableResult
mutating func remove(id: String) -> MeshResource.Part?
```

## See Also

- [var count: Int](meshpartcollection/count.md)
  Number of parts.
- [var isEmpty: Bool](meshpartcollection/isempty.md)
  True if there are no parts.
- [func insert(MeshResource.Part) -> Bool](meshpartcollection/insert(_:).md)
  Add a new part to the container. Returns true if added. Returns false if it already exists.
- [func removeAll()](meshpartcollection/removeall.md)
  Remove all the parts.
- [func update(MeshResource.Part) -> MeshResource.Part?](meshpartcollection/update(_:).md)
  Update an existing part. The old part is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/remove(id:))*