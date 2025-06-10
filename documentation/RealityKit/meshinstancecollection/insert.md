# insert(_:)

**Framework**: RealityKit  
**Kind**: method

Add a new instance to the container. Returns true if added. Returns false if it already exists.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@discardableResult
mutating func insert(_ instance: MeshResource.Instance) -> Bool
```

## See Also

- [var count: Int](meshinstancecollection/count.md)
  Number of instances.
- [var isEmpty: Bool](meshinstancecollection/isempty.md)
  True if there are no instances.
- [func remove(id:)](meshinstancecollection/remove(id:).md)
  Remove an instance by name.
- [func removeAll()](meshinstancecollection/removeall.md)
  Remove all the instances.
- [func update(_:)](meshinstancecollection/update(_:).md)
  Update an existing instance. The old instance is returned.
- [subscript(String) -> MeshResource.Instance?](meshinstancecollection/subscript(_:)-32e4c.md)
  Read an instance given its name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshinstancecollection/insert(_:))*