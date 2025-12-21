# removeAll()

**Framework**: RealityKit  
**Kind**: method

Remove all the models.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
mutating func removeAll()
```

## See Also

- [var count: Int](meshmodelcollection/count.md)
  Number of models.
- [var isEmpty: Bool](meshmodelcollection/isempty.md)
  True if there are no models.
- [func insert(MeshResource.Model) -> Bool](meshmodelcollection/insert(_:).md)
  Add a new model to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Model?](meshmodelcollection/remove(id:).md)
  Remove a model by id.
- [func update(MeshResource.Model) -> MeshResource.Model?](meshmodelcollection/update(_:).md)
  Update an existing model. The old model is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection/removeall())*