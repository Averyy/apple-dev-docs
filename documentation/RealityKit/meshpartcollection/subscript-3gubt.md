# subscript(_:)

**Framework**: RealityKit  
**Kind**: subscript

Read a part given its id.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
subscript(id: String) -> MeshResource.Part? { get }
```

## See Also

- [var count: Int](meshpartcollection/count.md)
  Number of parts.
- [var isEmpty: Bool](meshpartcollection/isempty.md)
  True if there are no parts.
- [func insert(_:)](meshpartcollection/insert(_:).md)
  Add a new part to the container. Returns true if added. Returns false if it already exists.
- [func remove(id:)](meshpartcollection/remove(id:).md)
  Remove a part by id.
- [func removeAll()](meshpartcollection/removeall.md)
  Remove all the parts.
- [func update(_:)](meshpartcollection/update(_:).md)
  Update an existing part. The old part is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/subscript(_:)-3gubt)*