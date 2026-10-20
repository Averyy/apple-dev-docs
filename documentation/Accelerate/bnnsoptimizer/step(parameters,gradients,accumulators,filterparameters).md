# step(parameters:gradients:accumulators:filterParameters:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
func step(parameters: [BNNSNDArrayDescriptor], gradients: [BNNSNDArrayDescriptor], accumulators: [BNNSNDArrayDescriptor], filterParameters: BNNSFilterParameters?) throws
```

## Default Implementations

### BNNSOptimizer Implementations
- [func step(parameters: [BNNSNDArrayDescriptor], gradients: [BNNSNDArrayDescriptor], accumulators: [BNNSNDArrayDescriptor], filterParameters: BNNSFilterParameters?) throws](./step%28parameters,gradients,accumulators,filterparameters%29-2zybm.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsoptimizer/step(parameters:gradients:accumulators:filterparameters:))*