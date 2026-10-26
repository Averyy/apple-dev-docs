---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedscenario/init(transcript:template:margin:configuration:innermodel:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(transcript:template:margin:configuration:innerModel:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

## Declaration

```swift
init(transcript: Transcript, template: any ScriptedChatTemplate = MinimalChatTemplate(), margin: ScriptedLogitsModel.Margin = .dominant, configuration: ModelConfiguration = ModelConfiguration(id: "scripted"), innerModel: (_ vocabularySize: Int) throws -> any LanguageModel) throws
```

## Parameters

- `transcript`: The conversation to script.
- `template`: The chat template; the generation prompt marks each assistant turn.
- `margin`: How strongly the model favors the scripted token.
- `configuration`: The context’s model configuration. Its `eosTokenIds` and `extraEOSTokens` are blocked after a script, like the tokenizer’s EOS.
- `innerModel`: Makes the wrapped model, given the vocabulary size it must support. Usually a small model with random weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedscenario/init(transcript:template:margin:configuration:innermodel:))*