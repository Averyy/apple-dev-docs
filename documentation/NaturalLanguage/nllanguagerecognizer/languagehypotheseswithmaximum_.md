# languageHypothesesWithMaximum:

**Framework**: Natural Language  
**Kind**: method  
**Role**: Instance Method

Generates the probabilities of possible languages for the processed text.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```objc
- (NSDictionary<NSString *,NSNumber *> *) languageHypothesesWithMaximum:(NSUInteger) maxHypotheses;
```

## Mentions

- [Identifying the language in text](../identifying-the-language-in-text.md)

## Return Value

A dictionary mapping languages with their probabilities, up to `maxHypotheses` languages.

## Parameters

- `maxHypotheses`: The maximum number of languages to return.

## See Also

### Determining the language
- [class func dominantLanguage(for: String) -> NLLanguage?](./dominantlanguage%28for%29.md)
  Finds the most likely language of a piece of text.
- [func processString(String)](./processstring%28_%29.md)
  Analyzes the piece of text to determine its dominant language.
- [var dominantLanguage: NLLanguage?](./dominantlanguage.md)
  The most likely language for the processed text.
- [func reset()](./reset%28%29.md)
  Resets the recognizer to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/languagehypotheseswithmaximum:)*