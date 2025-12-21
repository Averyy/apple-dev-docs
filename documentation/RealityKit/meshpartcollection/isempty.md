# isEmpty

**Framework**: RealityKit  
**Kind**: property

True if there are no parts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
var isEmpty: Bool { get }
```

## See Also

- [var count: Int](meshpartcollection/count.md)
  Number of parts.
- [func insert(MeshResource.Part) -> Bool](meshpartcollection/insert(_:).md)
  Add a new part to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Part?](meshpartcollection/remove(id:).md)
  Remove a part by id.
- [func removeAll()](meshpartcollection/removeall.md)
  Remove all the parts.
- [func update(MeshResource.Part) -> MeshResource.Part?](meshpartcollection/update(_:).md)
  Update an existing part. The old part is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/isempty)*