---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/deferredtokenlogprobabilities"
framework: "mlx-swift-lm/MLXLMCommon"
---

# DeferredTokenLogProbabilities

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Log probabilities for one generated token that are still on the GPU.

## Declaration

```swift
struct DeferredTokenLogProbabilities
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Overview

[`TokenIterator`](./tokeniterator.md) evaluates them with the decode step that samples the token. Handlers that ignore them skip the GPU-to-host copy. MLX arrays are not `Sendable`, so call [`materialize()`](./deferredtokenlogprobabilities/materialize%28%29.md) on the generation worker and send the result.

## Topics

### Instance Methods
- [func materialize() -> GenerateTokenLogProbabilities](./deferredtokenlogprobabilities/materialize%28%29.md)
  Copies the values from the GPU into a `Sendable` value.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/deferredtokenlogprobabilities)*