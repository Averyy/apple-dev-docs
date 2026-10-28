---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary"
framework: "mlx-swift-lm/MLXScriptedLM"
---

# ScriptedVocabulary

**Framework**: mlx-swift-lm/MLXScriptedLM  
**Kind**: struct  
**Role**: Structure

A deterministic vocabulary for scripted tests.

## Declaration

```swift
struct ScriptedVocabulary
```

## Overview

Id layout:

- `0 ..< reservedSpecialCount`: atomic special tokens, then `<|reserved_N|>` fillers
- next 256 ids: one byte-fallback token per byte value
- remaining ids: corpus pieces, in first-seen order

Every entry decodes to a fixed byte string, so `decode(encode(s)) == s` for any `s`.

## Topics

### Operators
- [static func == (ScriptedVocabulary, ScriptedVocabulary) -> Bool](./scriptedvocabulary/eqeq%28_,_%29.md)
### Instance Properties
- [var size: Int](./scriptedvocabulary/size.md)
### Instance Methods
- [func decode([Int], skipSpecialTokens: Bool) -> String](./scriptedvocabulary/decode%28_,skipspecialtokens%29.md)
  Concatenates token bytes. Invalid UTF-8 (a partial character) decodes to U+FFFD. Ids outside the vocabulary are ignored.
- [func encode(String) -> [Int]](./scriptedvocabulary/encode%28_%29.md)
  Longest-match encoding. Specials are matched first at every position, and a piece never extends over the start of a special. Unmatched bytes use byte fallback.
- [func id(forToken: String) -> Int?](./scriptedvocabulary/id%28fortoken%29.md)
  Id of a token by name: a special, a piece, or a byte (`"a"` or `"<0x0A>"`).
- [func isSpecial(Int) -> Bool](./scriptedvocabulary/isspecial%28_%29.md)
- [func specialID(String) -> Int?](./scriptedvocabulary/specialid%28_%29.md)
  Id of an atomic special token, or `nil`.
### Default Implementations
- [Equatable Implementations](./scriptedvocabulary/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Vocabulary
- [struct VocabularyBuilder](./vocabularybuilder.md)
  Builds a [`ScriptedVocabulary`](./scriptedvocabulary.md) from a scenario corpus.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxscriptedlm/scriptedvocabulary)*