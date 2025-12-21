# update(_:)

**Framework**: RealityKit  
**Kind**: method

Update an existing instance. The old instance is returned.

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
mutating func update(_ instance: MeshResource.Instance) -> MeshResource.Instance?
```

## See Also

- [var count: Int](meshinstancecollection/count.md)
  Number of instances.
- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.
- [func insert(MeshResource.Instance) -> Bool](meshinstancecollection/insert(_:).md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Instance?](meshinstancecollection/remove(id:).md)
  Remove an instance by name.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/update(_:))*