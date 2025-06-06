# BNNSMatMulWorkspaceSize(_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the workspace size that a matrix multiply operation requires.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
func BNNSMatMulWorkspaceSize(_ transA: Bool, _ transB: Bool, _ alpha: Float, _ inputA: UnsafePointer<BNNSNDArrayDescriptor>, _ inputB: UnsafePointer<BNNSNDArrayDescriptor>, _ output: UnsafePointer<BNNSNDArrayDescriptor>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> Int
```

#### Return Value

The required allocation size for workspace paramter to [`BNNSMatMul(_:_:_:_:_:_:_:_:)`](bnnsmatmul(_:_:_:_:_:_:_:_:).md), in bytes.

## Parameters

- `transA`: A Boolean value that specifies whether the operation should treat   as transposed.
- `transB`: A Boolean value that specifies whether the operation should treat   as transposed.
- `alpha`: A value that the operation uses to scale the result.
- `inputA`: A pointer to the   matrix descriptor.
- `inputB`: A pointer to the   matrix descriptor.
- `output`: A pointer to the output matrix descriptor.
- `filter_params`: The filter runtime parameters.

## See Also

- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:).md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [class BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
- [struct BNNSLayerParametersBroadcastMatMul](bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerbroadcastmatmul(_:_:).md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutableRawPointer?, UnsafePointer<BNNSFilterParameters>?) -> Int32](bnnsmatmul(_:_:_:_:_:_:_:_:).md)
  Applies a matrix multiplication operation directly to two input matrices.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](bnns/applymatrixmultiplication(inputa:transposed:inputb:transposed:output:alpha:workspace:filterparameters:).md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](bnns/matrixmultiplicationworkspacesize(inputa:transposed:inputb:transposed:output:alpha:filterparameters:).md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsmatmulworkspacesize(_:_:_:_:_:_:_:))*