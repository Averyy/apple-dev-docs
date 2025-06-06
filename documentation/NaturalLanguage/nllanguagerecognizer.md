# NLLanguageRecognizer

**Framework**: Natural Language  
**Kind**: class

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

## Mentions

- [Identifying the language in text](identifying-the-language-in-text.md)

#### Overview

An [`NLLanguageRecognizer`](nllanguagerecognizer.md) object automatically detects the language of a piece of text. It performs language identification by:

1. Identifying the dominant script of a piece of text. Some languages have a unique script (like Greek), but others share the same script (like English, French, and German, which all share the Latin script).
2. Identifying the language itself.

The identification obtained from an [`NLLanguageRecognizer`](nllanguagerecognizer.md) object can be either a single most likely language, access through [`dominantLanguage`](nllanguagerecognizer/dominantlanguage.md), or a set of language candidates with probabilities, using [`languageHypothesesWithMaximum:`](nllanguagerecognizer/languagehypotheseswithmaximum:.md). You can reset the recognizer to its initial state, to be reused for new analysis.

Use the convenience method, [`dominantLanguage(for:)`](nllanguagerecognizer/dominantlanguage(for:).md), to get the most likely language without creating an [`NLLanguageRecognizer`](nllanguagerecognizer.md).

> ❗ **Important**:  Don’t use an instance of [`NLLanguageRecognizer`](nllanguagerecognizer.md) from more than one thread simultaneously.

 Don’t use an instance of [`NLLanguageRecognizer`](nllanguagerecognizer.md) from more than one thread simultaneously.

## Topics

### Creating a recognizer
- [init()](nllanguagerecognizer/init.md)
  Creates a recognizer that you can customize.
### Determining the language
- [class func dominantLanguage(for: String) -> NLLanguage?](nllanguagerecognizer/dominantlanguage(for:).md)
  Finds the most likely language of a piece of text.
- [func processString(String)](nllanguagerecognizer/processstring(_:).md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](nllanguagerecognizer/dominantlanguage.md)
  The most likely language for the processed text.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](nllanguagerecognizer/languagehypotheses(withmaximum:).md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](nllanguagerecognizer/reset.md)
  Resets the recognizer to its initial state.
### Guiding the recognizer
- [var languageHints: [NLLanguage : Double]](nllanguagerecognizer/languagehints-7dwgv.md)
  A dictionary that maps languages to their probabilities in the language identification process.
- [var languageConstraints: [NLLanguage]](nllanguagerecognizer/languageconstraints.md)
  Limits the set of possible languages that the recognizer will return.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying the language in text](identifying-the-language-in-text.md)
  Detect the language in a piece of text by using a language recognizer.
- [struct NLLanguage](nllanguage.md)
  The languages that the Natural Language framework supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer)*