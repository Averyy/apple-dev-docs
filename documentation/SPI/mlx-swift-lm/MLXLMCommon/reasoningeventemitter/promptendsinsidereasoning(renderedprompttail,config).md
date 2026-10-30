---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/promptendsinsidereasoning(renderedprompttail:config:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# promptEndsInsideReasoning(renderedPromptTail:config:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Type Method

Whether a rendered prompt ends *inside* an open reasoning block — used to seed `primedInside`.

## Declaration

```swift
static func promptEndsInsideReasoning(renderedPromptTail tail: String, config: ReasoningConfig) -> Bool
```

## Discussion

The headline families (Qwen3 with thinking enabled, DeepSeek-R1) prefill the opening delimiter into the assistant generation prompt, so the model’s first generated token is already reasoning content and it never emits an opening `<think>` — only the closing `</think>`. An emitter started `Outside` would misroute the entire thought block to `.response` and leak a bare `</think>`.

The check must NOT be a naive `hasSuffix(startDelimiter)`: templates routinely append a trailing newline (`<think>\n`) after the prefill, so a strict suffix test returns false and silently misroutes 100% of reasoning. Instead: trim trailing whitespace, then require the prompt to end with the start delimiter, or for a labeled channel, with the start delimiter and a label.

A start delimiter followed by any other text came from earlier content, such as a user message or a tool result. A typed `<think>` tokenizes to the template’s own id, so only its position tells the two apart.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/reasoningeventemitter/promptendsinsidereasoning(renderedprompttail:config:))*