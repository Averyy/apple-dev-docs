# init(tagSchemes:options:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a linguistic tagger instance using the specified tag schemes and options.

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
init(tagSchemes: [NSLinguisticTagScheme], options opts: Int)
```

```objc
- (instancetype) initWithTagSchemes:(NSArray<NSString *> *) tagSchemes options:(NSUInteger) opts;
```

## Return Value

An initialized linguistic tagger.

## Discussion

Pass any tag schemes to `tagSchemes` that you intend to use with the methods described in Enumerating Linguistic Tags and Getting Linguistic Tags.

> 💡 **Tip**:  Avoid specifying tag schemes that you won’t use to ensure optimal performance.

## Parameters

- `tagSchemes`: An array of tag schemes to be used. See [`NSLinguisticTagScheme`](../nslinguistictagscheme.md) for the possible values.
- `opts`: Reserved for future use. Specify `0` for this parameter.

## See Also

### Related Documentation
- [struct NSLinguisticTagScheme](../nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
### First Steps
- [Tokenizing Natural Language Text](../tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [var string: String?](./string.md)
  The string being analyzed by the linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/init(tagschemes:options:))*