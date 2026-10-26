# languageConstraints

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

Limits the set of possible languages that the recognizer will return.

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
var languageConstraints: [NLLanguage] { get set }
```

```objc
@property (nonatomic, copy) NSArray<NSString *> * languageConstraints;
```

## See Also

### Guiding the recognizer
- [var languageHints: [NLLanguage : Double]](./languagehints-7dwgv.md)
  A dictionary that maps languages to their probabilities in the language identification process.
- [languageHints](./languagehints-3gy00.md)
  A dictionary that maps languages to their probabilities in the language identification process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/languageconstraints)*