---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedscaleddotproductattention(queries:quantizedkeys:quantizedvalues:scale:mask:groupsize:bits:mode:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# quantizedScaledDotProductAttention(queries:quantizedKeys:quantizedValues:scale:mask:groupSize:bits:mode:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

## Declaration

```swift
func quantizedScaledDotProductAttention(queries: MLXArray, quantizedKeys: (MLXArray, MLXArray, MLXArray?), quantizedValues: (MLXArray, MLXArray, MLXArray?), scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode = .none, groupSize: Int = 64, bits: Int = 8, mode: QuantizationMode = .affine) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedscaleddotproductattention(queries:quantizedkeys:quantizedvalues:scale:mask:groupsize:bits:mode:))*