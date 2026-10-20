# reshape(with:sourceArray:dimensionCount:dimensionSizes:destinationArray:)

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
func reshape(with cmdBuf: (any MTLCommandBuffer)?, sourceArray: MPSNDArray, dimensionCount numberOfDimensions: Int, dimensionSizes: UnsafeMutablePointer<Int>, destinationArray: MPSNDArray?) -> MPSNDArray?
```

```objc
- (MPSNDArray *) reshapeWithCommandBuffer:(id<MTLCommandBuffer>) cmdBuf sourceArray:(MPSNDArray *) sourceArray dimensionCount:(NSUInteger) numberOfDimensions dimensionSizes:(NSUInteger *) dimensionSizes destinationArray:(MPSNDArray *) destinationArray;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsndarrayidentity/reshape(with:sourcearray:dimensioncount:dimensionsizes:destinationarray:))*