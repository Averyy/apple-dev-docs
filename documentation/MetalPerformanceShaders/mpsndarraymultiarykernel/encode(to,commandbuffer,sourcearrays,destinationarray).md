# encode(to:commandBuffer:sourceArrays:destinationArray:)

**Framework**: Metal Performance Shaders  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func encode(to encoder: (any MTLComputeCommandEncoder)?, commandBuffer: any MTLCommandBuffer, sourceArrays: [MPSNDArray], destinationArray destination: MPSNDArray)
```

```objc
- (void) encodeToCommandEncoder:(id<MTLComputeCommandEncoder>) encoder commandBuffer:(id<MTLCommandBuffer>) commandBuffer sourceArrays:(NSArray<MPSNDArray *> *) sourceArrays destinationArray:(MPSNDArray *) destination;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarraymultiarykernel/encode(to:commandbuffer:sourcearrays:destinationarray:))*