# zone

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The zone, if any, from which this mesh buffer was created.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly, nullable) id<MDLMeshBufferZone> zone;
```

## Discussion

A single [`MTLBuffer`](../../Metal/mtlbuffer.md) object is allocated for each zone, but each zone can have multiple [`MTKMeshBuffer`](../mtkmeshbuffer.md) objects, each with its own [`offset`](./offset.md). Though there may be many [`MTKMeshBuffer`](../mtkmeshbuffer.md) objects for a model, they are all backed with the same contiguous [`MTLBuffer`](../../Metal/mtlbuffer.md) objects.

If a [`MTKMeshBufferAllocator`](../mtkmeshbufferallocator.md) object is used, Model I/O attempts to load all vertex and index data of a single mesh into a single zone. This allows the GPU to achieve a higher cache hit rate when drawing the mesh.

## See Also

### Originating Objects
- [var allocator: MTKMeshBufferAllocator](./allocator.md)
  The allocator object used to create this mesh buffer.
- [var type: MDLMeshBufferType](./type.md)
  The type of data contained in the originating Model I/O buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/zone)*