# dominantLanguage(for:)

**Framework**: Natural Language  
**Kind**: method

Finds the most likely language of a piece of text.

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
class func dominantLanguage(for string: String) -> NLLanguage?
```

#### Return Value

The most probable language of the piece of text.

## Parameters

- `string`: The text to analyze.

## See Also

- [func processString(String)](nllanguagerecognizer/processstring(_:).md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](nllanguagerecognizer/dominantlanguage.md)
  The most likely language for the processed text.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](nllanguagerecognizer/languagehypotheses(withmaximum:).md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](nllanguagerecognizer/reset.md)
  Resets the recognizer to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/dominantlanguage(for:))*