# temporaryResultState(commandBuffer:sourceImages:sourceStates:destinationImage:)

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
func temporaryResultState(commandBuffer: any MTLCommandBuffer, sourceImages sourceImage: [MPSImage], sourceStates: [MPSState]?, destinationImage: MPSImage) -> MPSState?
```

```objc
- (MPSState *) temporaryResultStateForCommandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceImages:(NSArray<MPSImage *> *) sourceImage sourceStates:(NSArray<MPSState *> *) sourceStates destinationImage:(MPSImage *) destinationImage;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnmultiarykernel/temporaryresultstate(commandbuffer:sourceimages:sourcestates:destinationimage:))*