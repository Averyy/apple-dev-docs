# SFCustomLanguageModelData.CustomPronunciation

**Framework**: Speech  
**Kind**: struct

A term to be introduced into the speech recognition model’s vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
struct CustomPronunciation
```

#### Overview

Attempts to add terms that are already in the model’s vocabulary will be ignored. Pronunciations that use X-SAMPA symbols that are not supported will be ignored; see [`supportedPhonemes(locale:)`](sfcustomlanguagemodeldata/supportedphonemes(locale:).md) for the set of supported symbols.

## Topics

### Creating a term
- [init(grapheme: String, phonemes: [String])](sfcustomlanguagemodeldata/custompronunciation/init(grapheme:phonemes:).md)
### Inspecting a term
- [let grapheme: String](sfcustomlanguagemodeldata/custompronunciation/grapheme.md)
  The written representation of the term, the way it is expected to appear in transcriptions.
- [let phonemes: [String]](sfcustomlanguagemodeldata/custompronunciation/phonemes.md)
  Zero or more phonetic representations of the term, given as X-SAMPA strings.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DataInsertable](datainsertable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](sfcustomlanguagemodeldata/insert(term:).md)
  Add a custom term to the vocabulary.
- [static func supportedPhonemes(locale: Locale) -> [String]](sfcustomlanguagemodeldata/supportedphonemes(locale:).md)
  List the supported subset of X-SAMPA pronunciations supported by this locale for the Speech framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/custompronunciation)*