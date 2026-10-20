# capacity

**Framework**: Model I/O  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The data capacity of the zone, in bytes.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var capacity: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger capacity;
```

#### Discussion

You specify the capacity of a zone when creating it with the [`newZone(_:)`](../mdlmeshbufferallocator/newzone%28_%29.md) method of a concrete class implementing the [`MDLMeshBufferAllocator`](../mdlmeshbufferallocator.md) protocol.

## See Also

### Inspecting a Zone
- [var allocator: any MDLMeshBufferAllocator](./allocator.md)
  The allocator object that created the zone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/modelio/mdlmeshbufferzone/capacity)*