---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationtransformer/makehandler(wrapping:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeHandler(wrapping:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Creates a fresh handler on each pass, including automatic tool restarts.

## Declaration

```swift
func makeHandler(wrapping base: TextToolTokenLoopHandler) -> Handler
```

## Mentions

- [Observing token log probabilities](../generation-observability.md)

## Discussion

Forward every base event exactly once and in order, exposing it through [`generation`](../generationproviding/generation.md). Preserve the base’s stop-token properties, dispositions, end-of-generation output, and completion metadata. Automatically dispatched tool-call events are consumed by the session.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generationtransformer/makehandler(wrapping:))*