# allocator

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The allocator object used to create this mesh buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allocator: MTKMeshBufferAllocator { get }
```

```objc
@property (nonatomic, readonly, nonnull) MTKMeshBufferAllocator * allocator;
```

## Discussion

The allocator uses Model I/O for copy and re-layout operations, such as when a new vertex descriptor is applied to an existing vertex buffer.

## See Also

### Originating Objects
- [var type: MDLMeshBufferType](./type.md)
  The type of data contained in the originating Model I/O buffer.
- [zone](./zone.md)
  The zone, if any, from which this mesh buffer was created.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/allocator)*