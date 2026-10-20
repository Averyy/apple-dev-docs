# BNNSDirectApplyBroadcastMatMul(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Applies a broadcast matrix multiplication operation directly to two input matrices.

**Availability**:
- iOS 14.0+ - Deprecated in 16.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- iPadOS 14.0+ - Deprecated in 16.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- Mac Catalyst 14.0+ - Deprecated in 16.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- macOS 11.0+ - Deprecated in 13.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- tvOS 14.0+ - Deprecated in 16.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))
- watchOS 7.0+ - Deprecated in 9.0 (renamed: BNNSMatMul(_:_:_:_:_:_:_:_:))

> **Deprecated**: Use [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](./bnnsmatmul%28_,_,_,_,_,_,_,_%29.md) instead.

## Declaration

```swift
func BNNSDirectApplyBroadcastMatMul(_ transA: Bool, _ transB: Bool, _ alpha: Float, _ inputA: UnsafePointer<BNNSNDArrayDescriptor>, _ inputB: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?)
```

```c
void BNNSDirectApplyBroadcastMatMul(const _Bool transA, const _Bool transB, const float alpha, const BNNSNDArrayDescriptor *inputA, const BNNSNDArrayDescriptor *inputB, const BNNSNDArrayDescriptor *output, const BNNSFilterParameters *filter_params);
```

## Parameters

- `transA`: A Boolean value that transposes the last two dimensions of matrix *A*.
- `transB`: A Boolean value that transposes the last two dimensions of matrix *B*.
- `alpha`: A value to scale the result.
- `inputA`: The descriptor of matrix *A*.
- `inputB`: The descriptor of matrix *B*.
- `output`: The descriptor of the output.
- `filter_params`: The filter runtime parameters.

## See Also

### Matrix multiplication
- [class BroadcastMatrixMultiplyLayer](./bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [struct BNNSLayerParametersBroadcastMatMul](./bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerbroadcastmatmul%28_,_%29.md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMulWorkspaceSize(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int](./bnnsmatmulworkspacesize%28_,_,_,_,_,_,_%29.md)
  Returns the workspace size that a matrix multiply operation requires.
- [func BNNSMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutableRawPointer?, UnsafePointer<BNNSFilterParameters>?) -> Int32](./bnnsmatmul%28_,_,_,_,_,_,_,_%29.md)
  Applies a matrix multiplication operation directly to two input matrices.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./bnns/applymatrixmultiplication%28inputa,transposed,inputb,transposed,output,alpha,workspace,filterparameters%29.md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](./bnns/matrixmultiplicationworkspacesize%28inputa,transposed,inputb,transposed,output,alpha,filterparameters%29.md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:))*