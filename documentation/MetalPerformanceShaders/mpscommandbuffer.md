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
- [convenience init(fromCommandQueue: any MTLCommandQueue)](mpscommandbuffer/init(fromcommandqueue:).md)
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
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [MTLCommandBuffer](../metal/mtlcommandbuffer.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscommandbuffer)*