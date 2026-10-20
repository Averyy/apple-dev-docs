# object(at:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Returns the top-level object at the specified index in the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func object(at index: Int) -> MDLObject
```

```objc
- (MDLObject *) objectAtIndex:(NSUInteger) index;
```

#### Return Value

The object at the specified index.

#### Discussion

An asset contains one or more top-level objects (instances of the [`MDLObject`](../mdlobject.md) class or one of its subclasses, such as [`MDLMesh`](../mdlmesh.md)), each of which may contain a hierarchy of child objects.

## Parameters

- `index`: An index in the asset’s list of top-level objects; between zero and the value of the [`count`](./count.md) property.

## See Also

### Working with Asset Content
- [subscript(Int) -> MDLObject?](./subscript%28_%29.md)
  Returns the top-level object at the specified index in the asset, using subscript syntax.
- [var count: Int](./count.md)
  The number of top-level objects in the asset.
- [func childObjects(of: AnyClass) -> [MDLObject]](./childobjects%28of%29.md)
  Returns all objects contained in the asset of the specified class.
- [func add(MDLObject)](./add%28_%29.md)
  Adds the specified object to the asset’s list of top-level objects.
- [func remove(MDLObject)](./remove%28_%29.md)
  Removes the specified object from the asset’s list of top-level objects.
- [var boundingBox: MDLAxisAlignedBoundingBox](./boundingbox.md)
  The minimum region entirely enclosing the asset’s contents.
- [func boundingBox(atTime: TimeInterval) -> MDLAxisAlignedBoundingBox](./boundingbox%28attime%29.md)
  Returns the minimum region entirely enclosing the asset’s contents at the specified time sample.
- [var url: URL?](./url.md)
  The URL from which the asset was loaded, if available.
- [var bufferAllocator: any MDLMeshBufferAllocator](./bufferallocator.md)
  An object responsible for allocating mesh vertex data loaded from the asset.
- [var vertexDescriptor: MDLVertexDescriptor?](./vertexdescriptor.md)
  The description of the vertex data format to be used for loading mesh data from the asset.
- [var masters: any MDLObjectContainerComponent](./masters.md)
  An array of objects that can be reused in the asset’s object hierarchy through instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/object(at:))*