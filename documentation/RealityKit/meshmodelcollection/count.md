# count

**Framework**: RealityKit  
**Kind**: property

Number of models.

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

- [var isEmpty: Bool](meshmodelcollection/isempty.md)
  True if there are no models.
- [func insert(_:)](meshmodelcollection/insert(_:).md)
  Add a new model to the container. Returns true if added. Returns false if it already exists.
- [func remove(id:)](meshmodelcollection/remove(id:).md)
  Remove a model by id.
- [func removeAll()](meshmodelcollection/removeall.md)
  Remove all the models.
- [func update(_:)](meshmodelcollection/update(_:).md)
  Update an existing model. The old model is returned.
- [subscript(String) -> MeshResource.Model?](meshmodelcollection/subscript(_:)-5xuaf.md)
  Read a model given its id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection/count)*