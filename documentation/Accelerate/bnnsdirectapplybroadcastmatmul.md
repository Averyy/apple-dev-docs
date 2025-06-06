# BNNSDirectApplyBroadcastMatMul(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies a broadcast matrix multiplication operation directly to two input matrices.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSDirectApplyBroadcastMatMul(_ transA: Bool, _ transB: Bool, _ alpha: Float, _ inputA: UnsafePointer<BNNSNDArrayDescriptor>, _ inputB: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?)
```

## Parameters

- `transA`: A Boolean value that transposes the last two dimensions of matrix  .
- `transB`: A Boolean value that transposes the last two dimensions of matrix  .
- `alpha`: A value to scale the result.
- `inputA`: The descriptor of matrix  .
- `inputB`: The descriptor of matrix  .
- `output`: The descriptor of the output.
- `filter_params`: The filter runtime parameters.

## See Also

- [class BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [struct BNNSLayerParametersBroadcastMatMul](bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerbroadcastmatmul(_:_:).md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMulWorkspaceSize(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int](bnnsmatmulworkspacesize(_:_:_:_:_:_:_:).md)
  Returns the workspace size that a matrix multiply operation requires.
- [func BNNSMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutableRawPointer?, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsmatmul(_:_:_:_:_:_:_:_:).md)
  Applies a matrix multiplication operation directly to two input matrices.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/applymatrixmultiplication(inputa:transposed:inputb:transposed:output:alpha:workspace:filterparameters:).md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](bnns/matrixmultiplicationworkspacesize(inputa:transposed:inputb:transposed:output:alpha:filterparameters:).md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:))*