# image(for:imageDescriptor:kernel:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func image(for cmdBuf: any MTLCommandBuffer, imageDescriptor descriptor: MPSImageDescriptor, kernel: MPSKernel) -> MPSImage
```

```objc
- (MPSImage *) imageForCommandBuffer:(id<MTLCommandBuffer>) cmdBuf imageDescriptor:(MPSImageDescriptor *) descriptor kernel:(MPSKernel *) kernel;
```

## See Also

### Instance Methods
- [func imageBatch(for: any MTLCommandBuffer, imageDescriptor: MPSImageDescriptor, kernel: MPSKernel, count: Int) -> [MPSImage]](./imagebatch%28for,imagedescriptor,kernel,count%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimageallocator/image(for:imagedescriptor:kernel:))*