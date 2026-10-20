# encodeBatch(commandBuffer:primaryImages:secondaryImages:destinationStates:destinationImages:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
func encodeBatch(commandBuffer: any MTLCommandBuffer, primaryImages: [MPSImage], secondaryImages: [MPSImage], destinationStates: [MPSCNNArithmeticGradientState], destinationImages: [MPSImage])
```

```objc
- (void) encodeBatchToCommandBuffer:(id<MTLCommandBuffer>) commandBuffer primaryImages:(MPSImageBatch *) primaryImages secondaryImages:(MPSImageBatch *) secondaryImages destinationStates:(MPSCNNArithmeticGradientStateBatch *) destinationStates destinationImages:(MPSImageBatch *) destinationImages;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnarithmetic/encodebatch(commandbuffer:primaryimages:secondaryimages:destinationstates:destinationimages:))*