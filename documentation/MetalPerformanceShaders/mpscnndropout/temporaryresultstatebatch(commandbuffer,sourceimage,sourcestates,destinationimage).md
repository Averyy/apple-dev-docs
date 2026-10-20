# temporaryResultStateBatch(commandBuffer:sourceImage:sourceStates:destinationImage:)

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
func temporaryResultStateBatch(commandBuffer: any MTLCommandBuffer, sourceImage: [MPSImage], sourceStates: [[MPSState]]?, destinationImage: [MPSImage]) -> [MPSCNNDropoutGradientState]?
```

```objc
- (MPSCNNDropoutGradientStateBatch *) temporaryResultStateBatchForCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImage:(MPSImageBatch *) sourceImage sourceStates:(NSArray<NSArray<MPSState *> *> *) sourceStates destinationImage:(MPSImageBatch *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropout/temporaryresultstatebatch(commandbuffer:sourceimage:sourcestates:destinationimage:))*