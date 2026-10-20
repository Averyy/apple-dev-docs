# bufferAllocator

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property

An object responsible for allocating mesh vertex data loaded from the asset.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var bufferAllocator: any MDLMeshBufferAllocator { get }
```

```objc
@property (nonatomic, retain, readonly) id<MDLMeshBufferAllocator> bufferAllocator;
```

#### Discussion

You specify an allocator when loading an asset with the [`init(url:vertexDescriptor:bufferAllocator:)`](./init%28url,vertexdescriptor,bufferallocator%29-1tchi.md) initializer. If you do not specify an allocator, or import an asset through other means, the [`MDLAsset`](../mdlasset.md) class uses an internal allocator object.

For example, to use the MetalKit framework for loading vertex data into GPU buffers for rendering with Metal, pass a [`MTKMeshBufferAllocator`](../../MetalKit/mtkmeshbufferallocator.md) object for the `bufferAllocator` parameter. By specifying an allocator, you ensure that mesh data is copied a minimal number of times between being read from a file and being loaded into GPU memory for rendering.

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
- [var vertexDescriptor: MDLVertexDescriptor?](./vertexdescriptor.md)
  The description of the vertex data format to be used for loading mesh data from the asset.
- [var masters: any MDLObjectContainerComponent](./masters.md)
  An array of objects that can be reused in the asset’s object hierarchy through instancing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlasset/bufferallocator)*