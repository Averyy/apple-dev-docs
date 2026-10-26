---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compile(shapeless:_:)-8vkh0"
framework: "mlx-swift-lm/MLXLMCommon"
---

# compile(shapeless:_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Compiles a function that reads nothing but its arguments.

## Declaration

```swift
func compile(shapeless: Bool = false, _ body: @escaping @Sendable ([MLXArray]) -> [MLXArray]) -> @Sendable ([MLXArray]) -> [MLXArray]
```

#### Discussion

Shadows MLX’s `compile` with a `@Sendable` body, which cannot capture an `MLXArray` or a `Module`. Use [`CompiledTrace`](./compiledtrace.md) for a body that has to read module weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/compile(shapeless:_:)-8vkh0)*