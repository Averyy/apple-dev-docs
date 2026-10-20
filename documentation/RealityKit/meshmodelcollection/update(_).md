# update(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Update an existing model. The old model is returned.

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
mutating func update(_ model: MeshResource.Model) -> MeshResource.Model?
```

## See Also

### Using the collection
- [func insert(MeshResource.Model) -> Bool](./insert%28_%29.md)
  Add a new model to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Model?](./remove%28id%29.md)
  Remove a model by id.
- [func removeAll()](./removeall%28%29.md)
  Remove all the models.
- [subscript(String) -> MeshResource.Model?](./subscript%28_%29.md)
  Read a model given its id.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshmodelcollection/update(_:))*