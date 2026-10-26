---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/keygroupsize"
framework: "mlx-swift-lm/MLXLMCommon"
---

# keyGroupSize

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Affine-K quantization group size. Defaults to 64, but callers that already know the head dimension (e.g. `maybeTurboQuantizeKVCache`) can pass a value pre-resolved via `resolvedKVQuantizationGroupSize` so kernels and quantization agree. Resolved (and possibly adjusted) against the actual head dimension the first time an affine-K encode runs, see `resolveAffineKeyGroupSize(headDim:)`.

## Declaration

```swift
var keyGroupSize: Int { get }
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/keygroupsize)*