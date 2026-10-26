---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils"
framework: "mlx-swift-lm/MLXLMCommon"
---

# WiredMemoryUtils

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Helpers for deriving wired memory budgets from real runtime measurements.

## Declaration

```swift
enum WiredMemoryUtils
```

## Topics

### Type Methods
- [static func tune(context: ModelContext, tokenCount: Int, parameters: GenerateParameters, seedText: String, resetPeakMemory: Bool) async throws -> WiredMemoryMeasurement](./wiredmemoryutils/tune%28context,tokencount,parameters,seedtext,resetpeakmemory%29.md)
  Measure weights, KV cache, and prefill workspace for the given model context.
- [static func tune(input: LMInput, context: ModelContext, parameters: GenerateParameters, resetPeakMemory: Bool) async throws -> WiredMemoryMeasurement](./wiredmemoryutils/tune%28input,context,parameters,resetpeakmemory%29.md)
  Measure weights, KV cache, and prefill workspace using a prepared input.
- [static func tune(userInput: UserInput, context: ModelContext, parameters: GenerateParameters, resetPeakMemory: Bool) async throws -> WiredMemoryMeasurement](./wiredmemoryutils/tune%28userinput,context,parameters,resetpeakmemory%29.md)
  Measure weights, KV cache, and prefill workspace using a user input.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/wiredmemoryutils)*