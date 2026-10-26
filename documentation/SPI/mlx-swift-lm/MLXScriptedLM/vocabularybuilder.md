---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# VocabularyBuilder

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

Builds a [`ScriptedVocabulary`](./scriptedvocabulary.md) from a scenario corpus.

## Declaration

```swift
struct VocabularyBuilder
```

#### Overview

Register specials and add every string a scenario will encode, then call [`build()`](./vocabularybuilder/build%28%29.md). Text is pretokenized at build time, after all specials are known, so special text is never absorbed into a corpus piece.

Pretokenization (ASCII-oriented, deterministic):

- a word is an optional leading space plus a run of ASCII letters and digits
- a whitespace run is its own piece
- ASCII punctuation is left to byte fallback
- non-ASCII characters follow [`multibyteCharacters`](./vocabularybuilder/configuration-swift.struct/multibytecharacters-swift.property.md)

Words and whitespace runs are chunked to [`maxPieceLength`](./vocabularybuilder/configuration-swift.struct/maxpiecelength.md) bytes so long words are always multi-token. Single-byte pieces are dropped: byte tokens cover them.

## Topics

### Structures
- [VocabularyBuilder.Configuration](./vocabularybuilder/configuration-swift.struct.md)
### Initializers
- [init(configuration: Configuration)](./vocabularybuilder/init%28configuration%29.md)
### Instance Properties
- [let configuration: Configuration](./vocabularybuilder/configuration-swift.property.md)
### Instance Methods
- [func add(text: String)](./vocabularybuilder/add%28text%29.md)
- [func add(texts: some Sequence<String>)](./vocabularybuilder/add%28texts%29.md)
- [func addSpecial(String, atomic: Bool)](./vocabularybuilder/addspecial%28_,atomic%29.md)
  Registers a marker such as `<|end|>` or `<think>`.
- [func build() -> ScriptedVocabulary](./vocabularybuilder/build%28%29.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Vocabulary
- [struct ScriptedVocabulary](./scriptedvocabulary.md)
  A deterministic vocabulary for scripted tests.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/vocabularybuilder)*