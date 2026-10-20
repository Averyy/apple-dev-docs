# BNNSMatMulWorkspaceSize(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns the workspace size that a matrix multiply operation requires.

**Availability**:
- iOS 16.0+ - Deprecated in 18.0
- iPadOS 16.0+ - Deprecated in 18.0
- Mac Catalyst 16.0+ - Deprecated in 18.0
- macOS 13.0+ - Deprecated in 15.0
- tvOS 16.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 9.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
func BNNSMatMulWorkspaceSize(_ transA: Bool, _ transB: Bool, _ alpha: Float, _ inputA: UnsafePointer<BNNSNDArrayDescriptor>, _ inputB: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int
```

```c
ssize_t BNNSMatMulWorkspaceSize(const _Bool transA, const _Bool transB, const float alpha, const BNNSNDArrayDescriptor *inputA, const BNNSNDArrayDescriptor *inputB, const BNNSNDArrayDescriptor *output, const BNNSFilterParameters *filter_params);
```

#### Return Value

The required allocation size for workspace paramter to [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](./bnnsmatmul%28_,_,_,_,_,_,_,_%29.md), in bytes.

## Parameters

- `transA`: A Boolean value that specifies whether the operation should treat `inputA` as transposed.
- `transB`: A Boolean value that specifies whether the operation should treat `inputB` as transposed.
- `alpha`: A value that the operation uses to scale the result.
- `inputA`: A pointer to the `inputA` matrix descriptor.
- `inputB`: A pointer to the `inputB` matrix descriptor.
- `output`: A pointer to the output matrix descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

### Matrix multiplication
- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](./bnnsdirectapplybroadcastmatmul%28_,_,_,_,_,_,_%29.md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [class BroadcastMatrixMultiplyLayer](./bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [struct BNNSLayerParametersBroadcastMatMul](./bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerbroadcastmatmul%28_,_%29.md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutableRawPointer?, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsmatmul%28_,_,_,_,_,_,_,_%29.md)
  Applies a matrix multiplication operation directly to two input matrices.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./bnns/applymatrixmultiplication%28inputa,transposed,inputb,transposed,output,alpha,workspace,filterparameters%29.md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](./bnns/matrixmultiplicationworkspacesize%28inputa,transposed,inputb,transposed,output,alpha,filterparameters%29.md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsmatmulworkspacesize(_:_:_:_:_:_:_:))*