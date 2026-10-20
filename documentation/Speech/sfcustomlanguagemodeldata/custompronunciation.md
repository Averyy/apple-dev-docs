# SFCustomLanguageModelData.CustomPronunciation

**Framework**: Speech  
**Kind**: struct  
**Role**: Structure

A term to be introduced into the speech recognition model’s vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.1+

## Declaration

```swift
struct CustomPronunciation
```

#### Overview

Attempts to add terms that are already in the model’s vocabulary will be ignored. Pronunciations that use X-SAMPA symbols that are not supported will be ignored; see [`supportedPhonemes(locale:)`](./supportedphonemes%28locale%29.md) for the set of supported symbols.

## Topics

### Creating a term
- [init(grapheme: String, phonemes: [String])](./custompronunciation/init%28grapheme,phonemes%29.md)
### Inspecting a term
- [let grapheme: String](./custompronunciation/grapheme.md)
  The written representation of the term, the way it is expected to appear in transcriptions.
- [let phonemes: [String]](./custompronunciation/phonemes.md)
  Zero or more phonetic representations of the term, given as X-SAMPA strings.

## Relationships

### Conforms To
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [DataInsertable](../datainsertable.md)
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Adding terms
- [func insert(term: SFCustomLanguageModelData.CustomPronunciation)](./insert%28term%29.md)
  Add a custom term to the vocabulary.
- [static func supportedPhonemes(locale: Locale) -> [String]](./supportedphonemes%28locale%29.md)
  List the supported subset of X-SAMPA pronunciations supported by this locale for the Speech framework.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/custompronunciation)*