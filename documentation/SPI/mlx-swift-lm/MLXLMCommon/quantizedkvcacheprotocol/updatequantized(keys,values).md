---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol/updatequantized(keys:values:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# updateQuantized(keys:values:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Update cache and return quantized tuples for maximum efficiency

## Declaration

```swift
func updateQuantized(keys: MLXArray, values: MLXArray) -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))
```

## Return Value

Quantized tuples (keys, values) as ((weight, scales, biases), (weight, scales, biases))

## Parameters

- `keys`: New key data to add to cache
- `values`: New value data to add to cache


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol/updatequantized(keys:values:))*