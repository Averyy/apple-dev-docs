# MPSCommandBuffer

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

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

```objc
@interface MPSCommandBuffer : NSObject
```

## Topics

### Initializers
- [init(commandBuffer: any MTLCommandBuffer)](./mpscommandbuffer/init%28commandbuffer%29.md)
- [convenience init(from: any MTLCommandQueue)](./mpscommandbuffer/init%28from%29.md)
- [convenience init(fromCommandQueue: any MTLCommandQueue)](./mpscommandbuffer/init%28fromcommandqueue%29.md)
### Instance Properties
- [var commandBuffer: any MTLCommandBuffer](./mpscommandbuffer/commandbuffer.md)
- [var heapProvider: (any MPSHeapProvider)?](./mpscommandbuffer/heapprovider.md)
- [var predicate: MPSPredicate?](./mpscommandbuffer/predicate.md)
- [var rootCommandBuffer: any MTLCommandBuffer](./mpscommandbuffer/rootcommandbuffer.md)
### Instance Methods
- [func commitAndContinue()](./mpscommandbuffer/commitandcontinue%28%29.md)
- [func prefetchHeap(forWorkloadSize: Int)](./mpscommandbuffer/prefetchheap%28forworkloadsize%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MTLCommandBuffer](../Metal/mtlcommandbuffer.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscommandbuffer)*