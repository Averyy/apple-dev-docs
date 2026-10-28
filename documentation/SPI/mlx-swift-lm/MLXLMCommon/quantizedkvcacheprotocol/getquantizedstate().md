---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol/getquantizedstate()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# getQuantizedState()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Get current quantized state without updating

## Declaration

```swift
func getQuantizedState() -> ((MLXArray, MLXArray, MLXArray?), (MLXArray, MLXArray, MLXArray?))?
```

## Return Value

Current quantized state, or nil if cache is empty

## Discussion

Useful for accessing cached data without adding new tokens.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedkvcacheprotocol/getquantizedstate())*