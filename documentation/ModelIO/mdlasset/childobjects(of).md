# childObjects(of:)

**Framework**: Model I/O  
**Kind**: method  
**Role**: Instance Method

Returns all objects contained in the asset of the specified class.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func childObjects(of objectClass: AnyClass) -> [MDLObject]
```

```objc
- (NSArray<MDLObject *> *) childObjectsOfClass:(Class) objectClass;
```

## Return Value

An array of objects of the specified type, or an empty array if no such objects exist.

## Discussion

This method searches the asset’s entire child object hierarchy to find all objects of the specified type contained in the asset.

## Parameters

- `objectClass`: A Model I/O class (that is, a subclass of [`MDLObject`](../mdlobject.md)) representing a type of object stored in the asset. For example, pass the [`MDLMesh`](../mdlmesh.md) class to find all 3D objects stored in the asset, or the [`MDLLight`](../mdllight.md) class to find all light sources.

## See Also

### Working with Asset Content
- [func object(at: Int) -> MDLObject](./object%28at%29.md)
  Returns the top-level object at the specified index in the asset.
- [subscript(Int) -> MDLObject?](./subscript%28_%29.md)
  Returns the top-level object at the specified index in the asset, using subscript syntax.
- [var count: Int](./count.md)
  The number of top-level objects in the asset.
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

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/childobjects(of:))*