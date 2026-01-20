# MPSCommandBuffer

**Framework**: Metal Performance Shaders  
**Kind**: class

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCommandBuffer
```

## Topics

### Initializers
- [init(commandBuffer: any MTLCommandBuffer)](mpscommandbuffer/init(commandbuffer:).md)
- [convenience init(from: any MTLCommandQueue)](mpscommandbuffer/init(from:).md)
### Instance Properties
- [var commandBuffer: any MTLCommandBuffer](mpscommandbuffer/commandbuffer.md)
- [var heapProvider: (any MPSHeapProvider)?](mpscommandbuffer/heapprovider.md)
- [var predicate: MPSPredicate?](mpscommandbuffer/predicate.md)
- [var rootCommandBuffer: any MTLCommandBuffer](mpscommandbuffer/rootcommandbuffer.md)
### Instance Methods
- [func commitAndContinue()](mpscommandbuffer/commitandcontinue.md)
- [func prefetchHeap(forWorkloadSize: Int)](mpscommandbuffer/prefetchheap(forworkloadsize:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MTLCommandBuffer](../Metal/MTLCommandBuffer.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscommandbuffer)*