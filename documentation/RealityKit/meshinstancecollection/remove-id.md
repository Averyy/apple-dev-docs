# remove(id:)

**Framework**: RealityKit  
**Kind**: method

Remove an instance by name.

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
mutating func remove(id: String) -> MeshResource.Instance?
```

## See Also

- [var count: Int](meshinstancecollection/count.md)
  Number of instances.
- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.
- [func insert(MeshResource.Instance) -> Bool](meshinstancecollection/insert(_:).md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.
- [func update(MeshResource.Instance) -> MeshResource.Instance?](meshinstancecollection/update(_:).md)
  Update an existing instance. The old instance is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/remove(id:))*