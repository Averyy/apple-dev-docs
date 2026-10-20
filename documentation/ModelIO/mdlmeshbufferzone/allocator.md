# allocator

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The allocator object that created the zone.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allocator: any MDLMeshBufferAllocator { get }
```

```objc
@property (nonatomic, readonly) id<MDLMeshBufferAllocator> allocator;
```

#### Discussion

Use the [`newZone(_:)`](../mdlmeshbufferallocator/newzone%28_%29.md) method of a concrete class implementing the [`MDLMeshBufferAllocator`](../mdlmeshbufferallocator.md) protocol to create a zone.

## See Also

### Inspecting a Zone
- [var capacity: Int](./capacity.md)
  The data capacity of the zone, in bytes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferzone/allocator)*