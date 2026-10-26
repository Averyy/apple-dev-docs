---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/parametervalidator"
framework: "mlx-swift-lm/MLXLMCommon"
---

# parameterValidator

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

Optional validation for constraints that depend on generation parameters.

## Declaration

```swift
var parameterValidator: (@Sendable (GenerateParameters) throws -> Void)?
```

#### Discussion

Validation runs before a token iterator performs prefill, so an invalid configuration fails without spending model work or mutating a cache.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationcomponents/parametervalidator)*