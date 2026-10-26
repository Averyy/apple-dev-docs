---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/init(transcript:tokenizer:stoptokens:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(transcript:tokenizer:stopTokens:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

Initialize the TurnScripts.

## Declaration

```swift
init(transcript: Transcript, tokenizer: ScriptedTokenizer, stopTokens: Set<Int> = []) throws
```

#### Discussion

The transcript’s assistant scripts, with the template’s generation prompt as the turn marker.

An assistant turn that follows a user turn ends its prompt with that user message, rendered alone. This assumes the template renders a lone user message without a default system prompt.

## Parameters

- `transcript`: The transcript
- `tokenizer`: The tokenizer
- `stopTokens`: Token ids that stop generation besides the tokenizer’s EOS


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/turnscripts/init(transcript:tokenizer:stoptokens:))*