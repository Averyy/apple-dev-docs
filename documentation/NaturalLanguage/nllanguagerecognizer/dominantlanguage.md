# dominantLanguage

**Framework**: Natural Language  
**Kind**: property

The most likely language for the processed text.

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
var dominantLanguage: NLLanguage? { get }
```

## Mentions

- [Identifying the language in text](identifying-the-language-in-text.md)

## See Also

- [class func dominantLanguage(for: String) -> NLLanguage?](nllanguagerecognizer/dominantlanguage(for:).md)
  Finds the most likely language of a piece of text.
- [func processString(String)](nllanguagerecognizer/processstring(_:).md)
  Analyzes the piece of text to determine its dominant language.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](nllanguagerecognizer/languagehypotheses(withmaximum:).md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](nllanguagerecognizer/reset.md)
  Resets the recognizer to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/dominantlanguage)*