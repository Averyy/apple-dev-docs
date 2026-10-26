---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcache/getquantizedstate()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# getQuantizedState()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Get current quantized keys and values as tuples (efficient access)

## Declaration

```swift
func getQuantizedState() -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))?
```

#### Return Value

Tuple of ((keyWeight, keyScales, keyBiases), (valueWeight, valueScales, valueBiases))


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcache/getquantizedstate())*