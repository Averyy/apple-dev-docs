---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningheuristics"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ReasoningHeuristics

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Pre-load heuristics for deciding whether a model identifier looks like a reasoning-capable family.

## Declaration

```swift
enum ReasoningHeuristics
```

## Overview

This is a standalone, opt-in helper — nothing in `MLXLMCommon` calls it. It exists for callers that need to guess reasoning capability from a repo id alone (e.g. before any model files are downloaded, when no other signal is available). Callers that have a stronger signal, or that simply declare their capabilities explicitly, should not use it.

It is intentionally NOT a provable superset of what actually resolves at load time: a model’s own [`ChatConventionsProviding`](./chatconventionsproviding.md) declaration keys on the model type, which this heuristic never sees. A community re-upload with a non-matching repo name but a reasoning model type resolves a `ReasoningConfig` yet may not match here. Callers who need a stricter guarantee should declare `.reasoning` themselves.

## Topics

### Type Methods
- [static func isLikelyReasoningModel(String) -> Bool](./reasoningheuristics/islikelyreasoningmodel%28_%29.md)
  Whether the model identifier looks like a reasoning-capable model.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningheuristics)*