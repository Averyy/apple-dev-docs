# remove(id:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Remove an instance by name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@discardableResult
mutating func remove(id: String) -> MeshResource.Instance?
```

## See Also

### Using the collection
- [func insert(MeshResource.Instance) -> Bool](./insert%28_%29.md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func removeAll()](./removeall%28%29.md)
  Remove all the instances.
- [func update(MeshResource.Instance) -> MeshResource.Instance?](./update%28_%29.md)
  Update an existing instance. The old instance is returned.
- [subscript(String) -> MeshResource.Instance?](./subscript%28_%29.md)
  Read an instance given its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/remove(id:))*