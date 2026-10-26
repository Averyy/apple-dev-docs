# dominantLanguage(for:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NLLanguage) dominantLanguageForString:(NSString *) string;
```

#### Return Value

The most probable language of the piece of text.

## Parameters

- `string`: The text to analyze.

## See Also

### Determining the language
- [func processString(String)](./processstring%28_%29.md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](./dominantlanguage.md)
  The most likely language for the processed text.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](./languagehypotheses%28withmaximum%29.md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](./reset%28%29.md)
  Resets the recognizer to its initial state.
- [- languageHypothesesWithMaximum:](./languagehypotheseswithmaximum_.md)
  Generates the probabilities of possible languages for the processed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/dominantlanguage(for:))*