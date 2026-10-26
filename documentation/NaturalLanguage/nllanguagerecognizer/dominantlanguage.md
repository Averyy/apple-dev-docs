# dominantLanguage

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NLLanguage dominantLanguage;
```

## Mentions

- [Identifying the language in text](../identifying-the-language-in-text.md)

## See Also

### Determining the language
- [class func dominantLanguage(for: String) -> NLLanguage?](./dominantlanguage%28for%29.md)
  Finds the most likely language of a piece of text.
- [func processString(String)](./processstring%28_%29.md)
  Analyzes the piece of text to determine its dominant language.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](./languagehypotheses%28withmaximum%29.md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](./reset%28%29.md)
  Resets the recognizer to its initial state.
- [- languageHypothesesWithMaximum:](./languagehypotheseswithmaximum_.md)
  Generates the probabilities of possible languages for the processed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/dominantlanguage)*