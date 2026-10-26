---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/prepare(input:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# prepare(input:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Prepare user input for generation.

## Declaration

```swift
func prepare(input: sending consuming UserInput) async throws -> sending LMInput
```

#### Return Value

Prepared language model input (transferred via `sending`)

#### Discussion

This method safely prepares input within the actor’s isolation, avoiding the need for closure-based `perform` calls.

> **Note**: The `sending` keyword indicates the return value is transferred (not shared), allowing non-Sendable types like `LMInput` to safely cross isolation boundaries.

## Parameters

- `input`: The user input to prepare


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/prepare(input:))*