# count

**Framework**: RealityKit  
**Kind**: property

Number of instances.

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

- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.
- [func insert(_:)](meshinstancecollection/insert(_:).md)
  Add a new instance to the container. Returns true if added. Returns false if it already exists.
- [func remove(id:)](meshinstancecollection/remove(id:).md)
  Remove an instance by name.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.
- [func update(_:)](meshinstancecollection/update(_:).md)
  Update an existing instance. The old instance is returned.
- [subscript(String) -> MeshResource.Instance?](meshinstancecollection/subscript(_:)-32e4c.md)
  Read an instance given its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/count)*