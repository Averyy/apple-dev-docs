# vertexDescriptor

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

The description of the vertex data format to be used for loading mesh data from the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var vertexDescriptor: MDLVertexDescriptor? { get }
```

```objc
@property (nonatomic, retain, readonly, nullable) MDLVertexDescriptor * vertexDescriptor;
```

#### Discussion

If you specify a vertex descriptor when loading an asset with the [`init(url:vertexDescriptor:bufferAllocator:)`](./init%28url,vertexdescriptor,bufferallocator%29-1tchi.md) initializer, Model I/O  automatically translates mesh vertex data loaded from the asset into the format described by that [`MDLVertexDescriptor`](../mdlvertexdescriptor.md) object. If you do not specify a vertex descriptor, or import an asset through other means, this property’s value is `nil`, and Model I/O  loads vertex data in whatever format is stored in the asset file.

## See Also

### Working with Asset Content
- [func object(at: Int) -> MDLObject](./object%28at%29.md)
  Returns the top-level object at the specified index in the asset.
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
- [var masters: any MDLObjectContainerComponent](./masters.md)
  An array of objects that can be reused in the asset’s object hierarchy through instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/vertexdescriptor)*