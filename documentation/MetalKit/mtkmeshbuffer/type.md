# type

**Framework**: MetalKit  
**Kind**: property  
**Role**: Instance Property

The type of data contained in the originating Model I/O buffer.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var type: MDLMeshBufferType { get }
```

```objc
@property (nonatomic, readonly) MDLMeshBufferType type;
```

#### Discussion

A [`MDLMeshBuffer`](../../ModelIO/mdlmeshbuffer.md) object can contain Model I/O mesh vertex data or submesh index data.

## See Also

### Originating Objects
- [var allocator: MTKMeshBufferAllocator](./allocator.md)
  The allocator object used to create this mesh buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalkit/mtkmeshbuffer/type)*