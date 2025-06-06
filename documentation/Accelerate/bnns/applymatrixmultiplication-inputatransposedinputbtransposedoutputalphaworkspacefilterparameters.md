# applyMatrixMultiplication(inputA:transposed:inputB:transposed:output:alpha:workspace:filterParameters:)

**Framework**: Accelerate  
**Kind**: method

Performs a matrix multiplication operation directly on two input matrices.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- watchOS 9.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed transposeA: Bool, inputB: BNNSNDArrayDescriptor, transposed transposeB: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters? = nil) throws
```

## Parameters

- `inputA`: The descriptor of matrix A.
- `transposeA`: A Boolean value that indicates whether the function transposes the last two dimensions of matrix A.
- `inputB`: The descriptor of matrix B.
- `transposeB`: A Boolean value that indicates whether the function transposes the last two dimensions of matrix B.
- `output`: The descriptor of the output.
- `alpha`: A scalar value that scales the result.
- `workspace`: A pointer to a memory region that the function uses as scratch space. This must have a size no less than the value that   returns.
- `filterParameters`: The filter runtime parameters.

## See Also

- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:).md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
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
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](bnns/matrixmultiplicationworkspacesize(inputa:transposed:inputb:transposed:output:alpha:filterparameters:).md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/applymatrixmultiplication(inputa:transposed:inputb:transposed:output:alpha:workspace:filterparameters:))*