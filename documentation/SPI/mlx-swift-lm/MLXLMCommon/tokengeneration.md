---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokengeneration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TokenGeneration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Represents the different stages or outputs of raw-token generation.

## Declaration

```swift
enum TokenGeneration
```

## Mentions

- [Observing token log probabilities](./generation-observability.md)

## Overview

This mirrors `Generation`, but yields raw token IDs instead of decoded text/tool calls.

## Topics

### Enumeration Cases
- [case info(GenerateCompletionInfo)](./tokengeneration/info%28_%29.md)
  Completion information summarizing token counts and performance metrics.
- [TokenGeneration.token(_:)](./tokengeneration/token%28_%29.md)
  A generated token ID.
### Instance Properties
- [var info: GenerateCompletionInfo?](./tokengeneration/info.md)
  Completion info or nil
- [var token: Int?](./tokengeneration/token.md)
  Token ID or nil
### Type Methods
- [static func collect([TokenGeneration]?, TokenGeneration) -> [TokenGeneration]](./tokengeneration/collect%28_,_%29.md)
  Reducer that can be used with `throttle()` to gather elements into a batch

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/tokengeneration)*