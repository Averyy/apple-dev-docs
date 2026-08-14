# MPSImageAllocator

**Framework**: Metal Performance Shaders  
**Kind**: protocol

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol MPSImageAllocator : NSSecureCoding, NSObjectProtocol
```

## Topics

### Instance Methods
- [func image(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel) -> MPSImage](mpsimageallocator/image(for:imagedescriptor:kernel:).md)
- [func imageBatch(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel, count: Int) -> [MPSImage]](mpsimageallocator/imagebatch(for:imagedescriptor:kernel:count:).md)

## Relationships

### Inherits From
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class func defaultAllocator() -> any MPSImageAllocator](mpsimage/defaultallocator.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageallocator)*