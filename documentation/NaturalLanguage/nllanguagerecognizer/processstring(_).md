# processString(_:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Analyzes the piece of text to determine its dominant language.

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
func processString(_ string: String)
```

```objc
- (void) processString:(NSString *) string;
```

## Mentions

- [Identifying the language in text](../identifying-the-language-in-text.md)

## Discussion

Use this method to process the provided text and to update the [`dominantLanguage`](./dominantlanguage.md) result and `languageHypotheses(withMaximum:)` probabilities.

## See Also

### Determining the language
- [class func dominantLanguage(for: String) -> NLLanguage?](./dominantlanguage%28for%29.md)
  Finds the most likely language of a piece of text.
- [var dominantLanguage: NLLanguage?](./dominantlanguage.md)
  The most likely language for the processed text.
- [func languageHypotheses(withMaximum: Int) -> [NLLanguage : Double]](./languagehypotheses%28withmaximum%29.md)
  Generates the probabilities of possible languages for the processed text.
- [func reset()](./reset%28%29.md)
  Resets the recognizer to its initial state.
- [- languageHypothesesWithMaximum:](./languagehypotheseswithmaximum_.md)
  Generates the probabilities of possible languages for the processed text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/processstring(_:))*