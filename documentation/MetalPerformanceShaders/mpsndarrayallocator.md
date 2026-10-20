# MPSNDArrayAllocator

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
protocol MPSNDArrayAllocator : NSCopying, NSSecureCoding, NSObjectProtocol
```

```objc
@protocol MPSNDArrayAllocator <NSObject, NSSecureCoding, NSCopying>
```

## Topics

### Instance Methods
- [func array(for: any MTLCommandBuffer, arrayDescriptor: MPSNDArrayDescriptor, kernel: MPSKernel) -> MPSNDArray](./mpsndarrayallocator/array%28for,arraydescriptor,kernel%29.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayallocator)*