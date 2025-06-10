# remove(id:)

**Framework**: RealityKit  
**Kind**: method

Remove an instance by name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func remove(id: String) -> MeshResource.Instance?
```

## See Also

- [var count: Int](meshinstancecollection/count.md)
  Number of instances.
- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.
- [func insert(_:)](meshinstancecollection/insert(_:).md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.
- [func update(_:)](meshinstancecollection/update(_:).md)
  Update an existing instance. The old instance is returned.
- [subscript(String) -> MeshResource.Instance?](meshinstancecollection/subscript(_:)-32e4c.md)
  Read an instance given its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/remove(id:))*