# languageHints

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

A dictionary that maps languages to their probabilities in the language identification process.

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
@property (nonatomic, copy) NSDictionary<NSString *,NSNumber *> * languageHints;
```

#### Discussion

This is a dictionary mapping languages to their probabilities and used by [`processString(_:)`](./processstring%28_%29.md).

## See Also

### Guiding the recognizer
- [var languageConstraints: [NLLanguage]](./languageconstraints.md)
  Limits the set of possible languages that the recognizer will return.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nllanguagerecognizer/languagehints-3gy00)*