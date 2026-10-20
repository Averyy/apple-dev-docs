# string

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The string being analyzed by the linguistic tagger.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.7+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
var string: String? { get set }
```

```objc
@property (retain, nullable) NSString * string;
```

## Mentions

- [Identifying Parts of Speech](../identifying-parts-of-speech.md)
- [Identifying People, Places, and Organizations](../identifying-people-places-and-organizations.md)
- [Tokenizing Natural Language Text](../tokenizing-natural-language-text.md)

## See Also

### First Steps
- [Tokenizing Natural Language Text](../tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [init(tagSchemes: [NSLinguisticTagScheme], options: Int)](./init%28tagschemes,options%29.md)
  Creates a linguistic tagger instance using the specified tag schemes and options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/string)*