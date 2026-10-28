---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/isparoquantmodel(directory:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# isParoQuantModel(directory:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Returns `true` if the model directory contains a ParoQuant checkpoint.

## Declaration

```swift
func isParoQuantModel(directory: URL) -> Bool
```

## Discussion

Inspects `config.json` for `quant_method == "paroquant"` in `quantization_config` and verifies a supported architecture is declared.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/isparoquantmodel(directory:))*