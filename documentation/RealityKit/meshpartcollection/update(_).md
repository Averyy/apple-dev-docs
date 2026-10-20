# update(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Update an existing part. The old part is returned.

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
mutating func update(_ part: MeshResource.Part) -> MeshResource.Part?
```

## See Also

### Using the collection
- [func insert(MeshResource.Part) -> Bool](./insert%28_%29.md)
  Add a new part to the container. Returns true if added. Returns false if it already exists.
- [func remove(id: String) -> MeshResource.Part?](./remove%28id%29.md)
  Remove a part by id.
- [func removeAll()](./removeall%28%29.md)
  Remove all the parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/update(_:))*