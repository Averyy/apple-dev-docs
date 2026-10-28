# NLLanguageRecognizer

**Framework**: Natural Language  
**Kind**: class  
**Role**: Class

The language of a body of text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
class NLLanguageRecognizer
```

```objc
@interface NLLanguageRecognizer : NSObject
```

## Mentions

- [Identifying the language in text](./identifying-the-language-in-text.md)

## Overview

An [`NLLanguageRecognizer`](./nllanguagerecognizer.md) object automatically detects the language of a piece of text. It performs language identification by:

1. Identifying the dominant script of a piece of text. Some languages have a unique script (like Greek), but others share the same script (like English, French, and German, which all share the Latin script).
2. Identifying the language itself.

The identification obtained from an [`NLLanguageRecognizer`](./nllanguagerecognizer.md) object can be either a single most likely language, accessed through [`dominantLanguage`](./nllanguagerecognizer/dominantlanguage.md), or a set of language candidates with probabilities, using [`languageHypotheses(withMaximum:)`](./nllanguagerecognizer/languagehypotheses%28withmaximum%29.md). You can reset the recognizer to its initial state, to be reused for new analysis.

Use the convenience method, [`dominantLanguage(for:)`](./nllanguagerecognizer/dominantlanguage%28for%29.md), to get the most likely language without creating an [`NLLanguageRecognizer`](./nllanguagerecognizer.md).

Language identification is most reliable for longer passages of text. For very short inputs of only a few words, accuracy is lower, and for some text there may be no well-defined answer at all. For example, personal names are shared across languages and don’t belong definitively to any one of them. When you work with short or ambiguous text, inspect the full set of candidates with [`languageHypotheses(withMaximum:)`](./nllanguagerecognizer/languagehypotheses%28withmaximum%29.md) rather than relying on a single [`dominantLanguage`](./nllanguagerecognizer/dominantlanguage.md).  When you have prior knowledge about the input, like a person’s preferred languages, bias the recognizer toward them with [`languageHints`](./nllanguagerecognizer/languagehints-3gy00.md), or limit it to a known set with [`languageConstraints`](./nllanguagerecognizer/languageconstraints.md).

> ❗ **Important**: Don’t use an instance of [`NLLanguageRecognizer`](./nllanguagerecognizer.md) from more than one thread simultaneously.

## Topics

### Creating a recognizer
- [init()](./nllanguagerecognizer/init%28%29.md)
  Creates a recognizer that you can customize.
### Determining the language
- [class func dominantLanguage(for: String) -> NLLanguage?](./nllanguagerecognizer/dominantlanguage%28for%29.md)
  Finds the most likely language of a piece of text.
- [func processString(String)](./nllanguagerecognizer/processstring%28_%29.md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](./nllanguagerecognizer/dominantlanguage.md)
  The most likely language for the processed text.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](./nllanguagerecognizer/languagehypotheses%28withmaximum%29.md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](./nllanguagerecognizer/reset%28%29.md)
  Resets the recognizer to its initial state.
- [- languageHypothesesWithMaximum:](./nllanguagerecognizer/languagehypotheseswithmaximum_.md)
  Generates the probabilities of possible languages for the processed text.
### Guiding the recognizer
- [var languageHints: [NLLanguage : Double]](./nllanguagerecognizer/languagehints-7dwgv.md)
  A dictionary that maps languages to their probabilities in the language identification process.
- [var languageConstraints: [NLLanguage]](./nllanguagerecognizer/languageconstraints.md)
  Limits the set of possible languages that the recognizer will return.
- [languageHints](./nllanguagerecognizer/languagehints-3gy00.md)
  A dictionary that maps languages to their probabilities in the language identification process.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Language identification
- [Identifying the language in text](./identifying-the-language-in-text.md)
  Detect the language in a piece of text by using a language recognizer.
- [struct NLLanguage](./nllanguage.md)
  The languages that the Natural Language framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer)*