# BNNSLayerParametersBroadcastMatMul

**Framework**: Accelerate  
**Kind**: struct

A set of parameters that define a broadcast matrix multiply layer.

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
struct BNNSLayerParametersBroadcastMatMul
```

## Topics

### Initializers
- [init(alpha: Float, beta: Float, transA: Bool, transB: Bool, quadratic: Bool, a_is_weights: Bool, b_is_weights: Bool, iA_desc: BNNSNDArrayDescriptor, iB_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor)](bnnslayerparametersbroadcastmatmul/init(alpha:beta:transa:transb:quadratic:a_is_weights:b_is_weights:ia_desc:ib_desc:o_desc:).md)
  Returns a new broadcast matrix multiply layer parameters structure from the specified parameters.
- [init()](bnnslayerparametersbroadcastmatmul/init.md)
  Returns a new broadcast matrix multiply layer parameters structure.
### Instance Properties
- [var alpha: Float](bnnslayerparametersbroadcastmatmul/alpha.md)
  A value to scale the result.
- [var beta: Float](bnnslayerparametersbroadcastmatmul/beta.md)
  A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- [var transA: Bool](bnnslayerparametersbroadcastmatmul/transa.md)
  A Boolean value that transposes the last two dimensions of matrix .
- [var transB: Bool](bnnslayerparametersbroadcastmatmul/transb.md)
  A Boolean value that transposes the last two dimensions of matrix .
- [var quadratic: Bool](bnnslayerparametersbroadcastmatmul/quadratic.md)
  A Boolean value that determines whether the operation multiplies matrix  by itself.
- [var a_is_weights: Bool](bnnslayerparametersbroadcastmatmul/a_is_weights.md)
  A Boolean value that determines whether to treat matrix  as weights.
- [var b_is_weights: Bool](bnnslayerparametersbroadcastmatmul/b_is_weights.md)
  A Boolean value that determines whether to treat matrix  as weights.
- [var iA_desc: BNNSNDArrayDescriptor](bnnslayerparametersbroadcastmatmul/ia_desc.md)
  The descriptor of matrix .
- [var iB_desc: BNNSNDArrayDescriptor](bnnslayerparametersbroadcastmatmul/ib_desc.md)
  The descriptor of matrix .
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersbroadcastmatmul/o_desc.md)
  The descriptor of the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](bnnsdirectapplybroadcastmatmul(_:_:_:_:_:_:_:).md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [class BroadcastMatrixMultiplyLayer](bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersbroadcastmatmul)*