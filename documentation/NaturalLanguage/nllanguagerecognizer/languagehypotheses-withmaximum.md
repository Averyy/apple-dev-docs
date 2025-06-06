# languageHypotheses(withMaximum:)

**Framework**: Natural Language  
**Kind**: method

Generates the probabilities of possible languages for the processed text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 12.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
@nonobjc
func languageHypotheses(withMaximum maxHypotheses: Int) -> [NLLanguage : Double]
```

#### Return Value

A dictionary mapping languages with their probabilities, up to `maxHypotheses` languages.

## Parameters

- `maxHypotheses`: The maximum number of languages to return.

## See Also

- [class func dominantLanguage(for: String) -> NLLanguage?](nllanguagerecognizer/dominantlanguage(for:).md)
  Finds the most likely language of a piece of text.
- [func processString(String)](nllanguagerecognizer/processstring(_:).md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](nllanguagerecognizer/dominantlanguage.md)
  The most likely language for the processed text.
- [func reset()](nllanguagerecognizer/reset.md)
  Resets the recognizer to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/languagehypotheses(withmaximum:))*