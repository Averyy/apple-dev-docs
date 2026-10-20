# reshape(with:commandBuffer:sourceArray:dimensionCount:dimensionSizes:destinationArray:)

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
func reshape(with encoder: (any MTLComputeCommandEncoder)?, commandBuffer cmdBuf: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount numberOfDimensions: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?
```

```objc
- (MPSNDArray *) reshapeWithCommandEncoder:(id<MTLComputeCommandEncoder>) encoder commandBuffer:(id<MTLCommandBuffer>) cmdBuf sourceArray:(MPSNDArray *) sourceArray dimensionCount:(NSUInteger) numberOfDimensions dimensionSizes:(NSUInteger *) dimensionSizes destinationArray:(MPSNDArray *) destinationArray;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity/reshape(with:commandbuffer:sourcearray:dimensioncount:dimensionsizes:destinationarray:))*