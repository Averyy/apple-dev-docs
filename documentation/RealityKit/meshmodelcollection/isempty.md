# isEmpty

**Framework**: RealityKit  
**Kind**: property

True if there are no models.

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

- [var count: Int](meshmodelcollection/count.md)
  Number of models.
- [func insert(MeshResource.Model) -> Bool](meshmodelcollection/insert(_:).md)
  Add a new model to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Model?](meshmodelcollection/remove(id:).md)
  Remove a model by id.
- [func removeAll()](meshmodelcollection/removeall.md)
  Remove all the models.
- [func update(MeshResource.Model) -> MeshResource.Model?](meshmodelcollection/update(_:).md)
  Update an existing model. The old model is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection/isempty)*