# zone

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The memory pool from which the buffer was created.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var zone: any MDLMeshBufferZone { get }
```

```objc
@property (nonatomic, retain, readonly) id<MDLMeshBufferZone> zone;
```

## Discussion

Use the [`newBuffer(from:data:type:)`](../mdlmeshbufferallocator/newbuffer%28from,data,type%29.md) or [`newBuffer(from:length:type:)`](../mdlmeshbufferallocator/newbuffer%28from,length,type%29.md) method of an allocator to reserve memory in a shared pool for multiple related buffers.

## See Also

### Inspecting a Buffer
- [var allocator: any MDLMeshBufferAllocator](./allocator.md)
  The allocator object that created the buffer.
- [var type: MDLMeshBufferType](./type.md)
  The type of data contained in a buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbuffer/zone)*