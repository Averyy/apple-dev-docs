# BNNSLayerParametersBroadcastMatMul

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A set of parameters that define a broadcast matrix multiply layer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSLayerParametersBroadcastMatMul
```

```c
typedef struct { ... } BNNSLayerParametersBroadcastMatMul;
```

## Topics

### Initializers
- [init(alpha: Float, beta: Float, transA: Bool, transB: Bool, quadratic: Bool, a_is_weights: Bool, b_is_weights: Bool, iA_desc: BNNSNDArrayDescriptor, iB_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor)](./bnnslayerparametersbroadcastmatmul/init%28alpha,beta,transa,transb,quadratic,a_is_weights,b_is_weights,ia_desc,ib_desc,o_desc%29.md)
  Returns a new broadcast matrix multiply layer parameters structure from the specified parameters.
- [init()](./bnnslayerparametersbroadcastmatmul/init%28%29.md)
  Returns a new broadcast matrix multiply layer parameters structure.
### Instance Properties
- [var alpha: Float](./bnnslayerparametersbroadcastmatmul/alpha.md)
  A value to scale the result.
- [var beta: Float](./bnnslayerparametersbroadcastmatmul/beta.md)
  A value, that must be either 0.0 or 1.0, you use to scale the existing output before the operation adds it to the result.
- [var transA: Bool](./bnnslayerparametersbroadcastmatmul/transa.md)
  A Boolean value that transposes the last two dimensions of matrix *A*.
- [var transB: Bool](./bnnslayerparametersbroadcastmatmul/transb.md)
  A Boolean value that transposes the last two dimensions of matrix *B*.
- [var quadratic: Bool](./bnnslayerparametersbroadcastmatmul/quadratic.md)
  A Boolean value that determines whether the operation multiplies matrix *A* by itself.
- [var a_is_weights: Bool](./bnnslayerparametersbroadcastmatmul/a_is_weights.md)
  A Boolean value that determines whether to treat matrix *A* as weights.
- [var b_is_weights: Bool](./bnnslayerparametersbroadcastmatmul/b_is_weights.md)
  A Boolean value that determines whether to treat matrix *B* as weights.
- [var iA_desc: BNNSNDArrayDescriptor](./bnnslayerparametersbroadcastmatmul/ia_desc.md)
  The descriptor of matrix *A*.
- [var iB_desc: BNNSNDArrayDescriptor](./bnnslayerparametersbroadcastmatmul/ib_desc.md)
  The descriptor of matrix *B*.
- [var o_desc: BNNSNDArrayDescriptor](./bnnslayerparametersbroadcastmatmul/o_desc.md)
  The descriptor of the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Matrix multiplication
- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](./bnnsdirectapplybroadcastmatmul%28_,_,_,_,_,_,_%29.md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [class BroadcastMatrixMultiplyLayer](./bnns/broadcastmatrixmultiplylayer.md)
  A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersbroadcastmatmul)*