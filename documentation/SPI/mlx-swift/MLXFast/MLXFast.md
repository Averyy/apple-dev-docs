---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast"
framework: "mlx-swift/MLXFast"
---

# MLXFast

**Framework**: mlx-swift/MLXFast  
**Kind**: module  
**Role**: Framework

## Topics

### Variables
- [let deprecationWarning: Void](./deprecationwarning.md)
### Functions
- [func RoPE(MLXArray, dimensions: Int, traditional: Bool, base: Float?, scale: Float, offset: Int, freqs: MLXArray?, stream: StreamOrDevice) -> MLXArray](./rope%28_,dimensions,traditional,base,scale,offset,freqs,stream%29.md)
  Optimized implementation of `NN.RoPE`.
- [func layerNorm(MLXArray, weight: MLXArray?, bias: MLXArray?, eps: Float, stream: StreamOrDevice) -> MLXArray](./layernorm%28_,weight,bias,eps,stream%29.md)
  Layer normalization.
- [func metalKernel(name: String, inputNames: [String], outputNames: [String], source: String, header: String, ensureRowContiguous: Bool, atomicOutputs: Bool) -> MLXFast.MLXFastKernel](./metalkernel%28name,inputnames,outputnames,source,header,ensurerowcontiguous,atomicoutputs%29.md)
  A jit-compiled custom Metal kernel defined from a source string.
- [func rmsNorm(MLXArray, weight: MLXArray, eps: Float, stream: StreamOrDevice) -> MLXArray](./rmsnorm%28_,weight,eps,stream%29.md)
  Root Mean Square normalization (RMS norm).
- [func scaledDotProductAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXArray?, memoryEfficientThreshold: Int?, stream: StreamOrDevice) -> MLXArray](./scaleddotproductattention%28queries,keys,values,scale,mask,memoryefficientthreshold,stream%29.md)
  A fast implementation of multi-head attention: `O = softmax(Q @ K.T, dim=-1) @ V`
### Type Aliases
- [typealias MLXFastKernel](./mlxfastkernel.md)
  Container for a kernel created by [`metalKernel(name:inputNames:outputNames:source:header:ensureRowContiguous:atomicOutputs:)`](./metalkernel%28name,inputnames,outputnames,source,header,ensurerowcontiguous,atomicoutputs%29.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxfast)*