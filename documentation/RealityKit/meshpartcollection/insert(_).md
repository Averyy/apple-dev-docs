# insert(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Add a new part to the container. Returns true if added. Returns false if it already exists.

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
mutating func insert(_ part: MeshResource.Part) -> Bool
```

## See Also

### Using the collection
- [func remove(id: String) -> MeshResource.Part?](./remove%28id%29.md)
  Remove a part by id.
- [func removeAll()](./removeall%28%29.md)
  Remove all the parts.
- [func update(MeshResource.Part) -> MeshResource.Part?](./update%28_%29.md)
  Update an existing part. The old part is returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshpartcollection/insert(_:))*