---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(transcript:template:specials:textmarkers:configuration:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(transcript:template:specials:textMarkers:configuration:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

Builds a tokenizer whose vocabulary covers the transcript’s text.

## Declaration

```swift
init(transcript: Transcript, template: any ScriptedChatTemplate = MinimalChatTemplate(), specials: [String] = [], textMarkers: [String] = [], configuration: VocabularyBuilder.Configuration = .init())
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(transcript:template:specials:textmarkers:configuration:))*