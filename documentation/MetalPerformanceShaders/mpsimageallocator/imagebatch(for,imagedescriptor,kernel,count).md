# imageBatch(for:imageDescriptor:kernel:count:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func imageBatch(for cmdBuf: any MTLCommandBuffer, imageDescriptor descriptor: MPSImageDescriptor, kernel: MPSKernel, count: Int) -> [MPSImage]
```

```objc
- (MPSImageBatch *) imageBatchForCommandBuffer:(id<MTLCommandBuffer>) cmdBuf imageDescriptor:(MPSImageDescriptor *) descriptor kernel:(MPSKernel *) kernel count:(NSUInteger) count;
```

## See Also

### Instance Methods
- [func image(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel) -> MPSImage](./image%28for,imagedescriptor,kernel%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageallocator/imagebatch(for:imagedescriptor:kernel:count:))*