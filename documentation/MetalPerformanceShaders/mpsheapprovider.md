# MPSHeapProvider

**Framework**: Metal Performance Shaders  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
protocol MPSHeapProvider : NSObjectProtocol
```

```objc
@protocol MPSHeapProvider <NSObject>
```

## Topics

### Instance Methods
- [func newHeap(with: MTLHeapDescriptor) -> (any MTLHeap)?](./mpsheapprovider/newheap%28with%29.md)
- [func retire(any MTLHeap, cacheDelay: Double)](./mpsheapprovider/retire%28_,cachedelay%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsheapprovider)*