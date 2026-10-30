---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generation/reasoning(_:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# Generation.reasoning(_:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: case  
**Role**: Case

Thinking text, delivered separately from the answer and with the protocol’s delimiters already removed.

## Declaration

```swift
case reasoning(String)
```

## Discussion

Only produced for models whose response protocol frames reasoning: a resolved [`reasoningConfig`](../modelconfiguration/reasoningconfig.md) (`<think>` families, Gemma 4’s labeled channels) or a framed token protocol that carries its own reasoning channel (GPT-OSS Harmony, Onyx).

Reasoning is *not* part of [`chunk`](./chunk.md), so a caller recording the assistant turn should record [`chunk`](./chunk.md) alone as its content. Most of these families’ chat templates drop reasoning from replayed history. [`ChatSession`](../chatsession.md) keeps a finished thought beside the message for the templates that replay it.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generation/reasoning(_:))*