---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobability"
framework: "mlx-swift-lm/MLXLMCommon"
---

# GenerateTokenLogProbability

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The log probability assigned to one vocabulary token.

## Declaration

```swift
struct GenerateTokenLogProbability
```

## Topics

### Initializers
- [init(token: Int, logProbability: Float)](./generatetokenlogprobability/init%28token,logprobability%29.md)
### Instance Properties
- [let logProbability: Float](./generatetokenlogprobability/logprobability.md)
  The token’s log probability after logit processing and before sampling.
- [let token: Int](./generatetokenlogprobability/token.md)
  The vocabulary token ID.
### Default Implementations
- [Equatable Implementations](./generatetokenlogprobability/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generatetokenlogprobability)*