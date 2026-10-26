---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace/body"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CompiledTrace.Body

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: typealias  
**Role**: Type Alias

The traced body. Receives the owner whose weights it may read.

## Declaration

```swift
typealias Body = @Sendable (Owner, [MLXArray]) -> [MLXArray]
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compiledtrace/body)*