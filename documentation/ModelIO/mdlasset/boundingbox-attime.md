# boundingBox(atTime:)

**Framework**: Model I/O  
**Kind**: method

Returns the minimum region entirely enclosing the asset’s contents at the specified time sample.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func boundingBox(atTime time: TimeInterval) -> MDLAxisAlignedBoundingBox
```

#### Return Value

The asset’s bounding box as of the specified time sample.

#### Discussion

If an asset does not contain timed information, calling this method with any time sample is equivalent to reading the [`boundingBox`](mdlasset/boundingbox.md) property.

All assets can provide bounding box information without traversing their hierarchy of objects.

## Parameters

- `time`: A timestamp referring to timed information in the asset.

## See Also

- [func object(at: Int) -> MDLObject](mdlasset/object(at:).md)
  Returns the top-level object at the specified index in the asset.
- [subscript(Int) -> MDLObject?](mdlasset/subscript(_:).md)
  Returns the top-level object at the specified index in the asset, using subscript syntax.
- [var count: Int](mdlasset/count.md)
  The number of top-level objects in the asset.
- [func childObjects(of: AnyClass) -> [MDLObject]](mdlasset/childobjects(of:).md)
  Returns all objects contained in the asset of the specified class.
- [func add(MDLObject)](mdlasset/add(_:).md)
  Adds the specified object to the asset’s list of top-level objects.
- [func remove(MDLObject)](mdlasset/remove(_:).md)
  Removes the specified object from the asset’s list of top-level objects.
- [var boundingBox: MDLAxisAlignedBoundingBox](mdlasset/boundingbox.md)
  The minimum region entirely enclosing the asset’s contents.
- [var url: URL?](mdlasset/url.md)
  The URL from which the asset was loaded, if available.
- [var bufferAllocator: any MDLMeshBufferAllocator](mdlasset/bufferallocator.md)
  An object responsible for allocating mesh vertex data loaded from the asset.
- [var vertexDescriptor: MDLVertexDescriptor?](mdlasset/vertexdescriptor.md)
  The description of the vertex data format to be used for loading mesh data from the asset.
- [var masters: any MDLObjectContainerComponent](mdlasset/masters.md)
  An array of objects that can be reused in the asset’s object hierarchy through instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/boundingbox(attime:))*