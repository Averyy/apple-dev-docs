# MPSImageAllocator

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
protocol MPSImageAllocator : NSSecureCoding, NSObjectProtocol
```

```objc
@protocol MPSImageAllocator <NSObject, NSSecureCoding>
```

## Topics

### Instance Methods
- [func image(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel) -> MPSImage](./mpsimageallocator/image%28for,imagedescriptor,kernel%29.md)
- [func imageBatch(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel, count: Int) -> [MPSImage]](./mpsimageallocator/imagebatch%28for,imagedescriptor,kernel,count%29.md)

## Relationships

### Inherits From
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Methods to Get an Image Allocator
- [class func defaultAllocator() -> any MPSImageAllocator](./mpsimage/defaultallocator%28%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageallocator)*