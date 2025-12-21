# update(_:)

**Framework**: RealityKit  
**Kind**: method

Update an existing model. The old model is returned.

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
mutating func update(_ model: MeshResource.Model) -> MeshResource.Model?
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
- [func removeAll()](meshmodelcollection/removeall.md)
  Remove all the models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection/update(_:))*