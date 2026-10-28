---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/appendingparametervalidator(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# appendingParameterValidator(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Return a copy with an additional generation-parameter validator.

## Declaration

```swift
func appendingParameterValidator(_ validator: @escaping @Sendable (GenerateParameters) throws -> Void) -> GenerationComponents
```

## Discussion

Validators run in insertion order. This composes independently from the logit-processor chain so behavioral components can reject incompatible token limits before generation starts.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/appendingparametervalidator(_:))*