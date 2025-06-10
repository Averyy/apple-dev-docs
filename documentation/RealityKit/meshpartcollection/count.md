# count

**Framework**: RealityKit  
**Kind**: property

Number of parts.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
var count: Int { get }
```

## See Also

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
- [subscript(String) -> MeshResource.Part?](meshpartcollection/subscript(_:)-3gubt.md)
  Read a part given its id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/count)*