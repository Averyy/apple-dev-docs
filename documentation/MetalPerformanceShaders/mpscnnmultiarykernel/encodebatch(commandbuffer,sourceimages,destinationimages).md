# encodeBatch(commandBuffer:sourceImages:destinationImages:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, sourceImages: [[MPSImage]], destinationImages: [MPSImage])
```

```objc
- (void) encodeBatchToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(NSArray<NSArray<MPSImage *> *> *) sourceImages destinationImages:(MPSImageBatch *) destinationImages;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel/encodebatch(commandbuffer:sourceimages:destinationimages:))*