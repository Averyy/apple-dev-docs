---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel/init(wrapping:scripts:margin:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(wrapping:scripts:margin:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(wrapping wrapped: any LanguageModel, scripts: TurnScripts, margin: Margin = .dominant)
```

## Parameters

- `wrapped`: The model that computes the background logits. Its vocabulary must be at least as large as the largest scripted token id.
- `scripts`: The tokens to emit on each assistant turn.
- `margin`: How strongly to boost the scripted token.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedlogitsmodel/init(wrapping:scripts:margin:))*