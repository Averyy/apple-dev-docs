# insert(term:)

**Framework**: Speech  
**Kind**: method

Add a custom term to the vocabulary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.1+

## Declaration

```swift
func insert(term: SFCustomLanguageModelData.CustomPronunciation)
```

#### Discussion

This class accumulates vocabulary data (in the form of tokens paired with X-SAMPA representations of the spoken forms of those tokens) which will later be processed and then provided to an `SFSpeechRecognizer`, to enable it to recognize words that are typically out-of-vocabulary.

## Parameters

- `term`: A token, paired with an X-SAMPA representation of the token’s pronunciation

## See Also

- [static func supportedPhonemes(locale: Locale) -> [String]](sfcustomlanguagemodeldata/supportedphonemes(locale:).md)
  List the supported subset of X-SAMPA pronunciations supported by this locale for the Speech framework.
- [SFCustomLanguageModelData.CustomPronunciation](sfcustomlanguagemodeldata/custompronunciation.md)
  A term to be introduced into the speech recognition model’s vocabulary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/sfcustomlanguagemodeldata/insert(term:))*