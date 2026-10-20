# BNNS.BroadcastMatrixMultiplyLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a broadcast matrix multiply filter and manages its deinitialization.

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
class BroadcastMatrixMultiplyLayer
```

## Topics

### Creating a Broadcast Matrix Multiplication Layer
- [convenience init?(inputA: BNNSNDArrayDescriptor, transposed: Bool, isWeights: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, isWeights: Bool, output: BNNSNDArrayDescriptor, alpha: Float, accumulatesToOutput: Bool, isQuadratic: Bool, filterParameters: BNNSFilterParameters?)](./broadcastmatrixmultiplylayer/init%28inputa,transposed,isweights,inputb,transposed,isweights,output,alpha,accumulatestooutput,isquadratic,filterparameters%29.md)
  Returns a new broadcast matrix multiply layer.
### Applying a Broadcast Matrix Multiplication Layer
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor) throws](./broadcastmatrixmultiplylayer/applybackward%28batchsize,inputa,inputb,output,outputgradient,generatinginputagradient,generatinginputbgradient%29.md)
  Applies the layer backward to generate input gradients.
### Instance Methods
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](./broadcastmatrixmultiplylayer/apply%28batchsize,inputa,inputb,output%29.md)

## Relationships

### Inherits From
- [BNNS.Layer](./layer.md)

## See Also

### Matrix multiplication
- [func BNNSDirectApplyBroadcastMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?)](../bnnsdirectapplybroadcastmatmul%28_,_,_,_,_,_,_%29.md)
  Applies a broadcast matrix multiplication operation directly to two input matrices.
- [struct BNNSLayerParametersBroadcastMatMul](../bnnslayerparametersbroadcastmatmul.md)
  A set of parameters that define a broadcast matrix multiply layer.
- [func BNNSFilterCreateLayerBroadcastMatMul(UnsafePointer<BNNSLayerParametersBroadcastMatMul>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatelayerbroadcastmatmul%28_,_%29.md)
  Returns a new broadcast matrix multiply layer.
- [func BNNSMatMulWorkspaceSize(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSFilterParameters>?) -> Int](../bnnsmatmulworkspacesize%28_,_,_,_,_,_,_%29.md)
  Returns the workspace size that a matrix multiply operation requires.
- [func BNNSMatMul(Bool, Bool, Float, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafePointer<BNNSNDArrayDescriptor>, UnsafeMutableRawPointer?, UnsafePointer<BNNSFilterParameters>?) -> Int32](../bnnsmatmul%28_,_,_,_,_,_,_,_%29.md)
  Applies a matrix multiplication operation directly to two input matrices.
- [static func applyMatrixMultiplication(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, workspace: UnsafeMutableRawBufferPointer?, filterParameters: BNNSFilterParameters?) throws](./applymatrixmultiplication%28inputa,transposed,inputb,transposed,output,alpha,workspace,filterparameters%29.md)
  Performs a matrix multiplication operation directly on two input matrices.
- [static func matrixMultiplicationWorkspaceSize(inputA: BNNSNDArrayDescriptor, transposed: Bool, inputB: BNNSNDArrayDescriptor, transposed: Bool, output: BNNSNDArrayDescriptor, alpha: Float, filterParameters: BNNSFilterParameters?) -> Int?](./matrixmultiplicationworkspacesize%28inputa,transposed,inputb,transposed,output,alpha,filterparameters%29.md)
  Returns the workspace size that a matrix multiply operation requires.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/broadcastmatrixmultiplylayer)*