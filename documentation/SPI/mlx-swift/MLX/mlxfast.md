---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast"
framework: "mlx-swift/MLX"
---

# MLXFast

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum MLXFast
```

## Topics

### Classes
- [MLXFast.MLXFastKernel](./mlxfast/mlxfastkernel.md)
  Container for a kernel created by [`callAsFunction(_:template:grid:threadGroup:outputShapes:outputDTypes:initValue:verbose:stream:)`](./mlxfast/mlxfastkernel/callasfunction%28_,template,grid,threadgroup,outputshapes,outputdtypes,initvalue,verbose,stream%29.md)
### Type Methods
- [static func RoPE(MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: MLXArray, freqs: MLXArray?, stream: StreamOrDevice) -> MLXArray](./mlxfast/rope%28_,dimensions,traditional,base,scale,offset,freqs,stream%29-1u6i8.md)
  Optimized implementation of `NN.RoPE` with array offset for batched inference.
- [static func RoPE(MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: Int, freqs: MLXArray?, stream: StreamOrDevice) -> MLXArray](./mlxfast/rope%28_,dimensions,traditional,base,scale,offset,freqs,stream%29-52tkq.md)
  Optimized implementation of `NN.RoPE`.
- [static func crossEntropy(logits: MLXArray, targets: MLXArray, stream: StreamOrDevice) -> MLXArray](./mlxfast/crossentropy%28logits,targets,stream%29.md)
  Cross entropy loss with class indices as targets.
- [static func layerNorm(MLXArray, weight: MLXArray?, bias: MLXArray?, eps: Float, stream: StreamOrDevice) -> MLXArray](./mlxfast/layernorm%28_,weight,bias,eps,stream%29.md)
  Layer normalization.
- [static func metalKernel(name: String, inputNames: some Sequence<String>, outputNames: some Sequence<String>, source: String, header: String, ensureRowContiguous: Bool, atomicOutputs: Bool) -> MLXFast.MLXFastKernel](./mlxfast/metalkernel%28name,inputnames,outputnames,source,header,ensurerowcontiguous,atomicoutputs%29.md)
  A jit-compiled custom Metal kernel defined from a source string.
- [static func rmsNorm(MLXArray, weight: MLXArray, eps: Float, stream: StreamOrDevice) -> MLXArray](./mlxfast/rmsnorm%28_,weight,eps,stream%29.md)
  Root Mean Square normalization (RMS norm).
- [static func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode, sinks: MLXArray?, forceFused: Bool, stream: StreamOrDevice) -> MLXArray](./mlxfast/scaleddotproductattention%28queries,keys,values,scale,mask,sinks,forcefused,stream%29.md)
  A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`
- [static func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXArray?, sinks: MLXArray?, memoryEfficientThreshold: Int?, forceFused: Bool, stream: StreamOrDevice) -> MLXArray](./mlxfast/scaleddotproductattention%28queries,keys,values,scale,mask,sinks,memoryefficientthreshold,forcefused,stream%29.md)
  A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`
### Enumerations
- [MLXFast.ScaledDotProductAttentionMaskMode](./mlxfast/scaleddotproductattentionmaskmode.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/mlxfast)*