# languageHints

**Framework**: Natural Language  
**Kind**: property

A dictionary that maps languages to their probabilities in the language identification process.

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
var languageHints: [NLLanguage : Double] { get set }
```

#### Discussion

This is a dictionary mapping languages to their probabilities and used by [`processString(_:)`](nllanguagerecognizer/processstring(_:).md).

## See Also

- [var languageConstraints: [NLLanguage]](nllanguagerecognizer/languageconstraints.md)
  Limits the set of possible languages that the recognizer will return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/languagehints-7dwgv)*