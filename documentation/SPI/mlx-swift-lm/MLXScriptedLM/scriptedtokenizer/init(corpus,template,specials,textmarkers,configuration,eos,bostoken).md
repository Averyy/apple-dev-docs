---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(corpus:template:specials:textmarkers:configuration:eos:bostoken:)"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# init(corpus:template:specials:textMarkers:configuration:eos:bosToken:)

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: init  
**Role**: Initializer

Builds the vocabulary from `corpus` plus everything the template declares.

## Declaration

```swift
init(corpus: [String], template: any ScriptedChatTemplate = MinimalChatTemplate(), specials: [String] = [], textMarkers: [String] = [], configuration: VocabularyBuilder.Configuration = .init(), eos: EndOfSequence = .template, bosToken: String? = nil)
```

#### Discussion

The corpus should hold every string a test will encode, so it tokenizes into corpus pieces rather than byte fallback. Unlisted text still round-trips. `specials` and `textMarkers` are for markers the scenario adds itself, such as `<think>`; the template’s own markers need not be listed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedtokenizer/init(corpus:template:specials:textmarkers:configuration:eos:bostoken:))*