# init(tagSchemes:options:)

**Framework**: Foundation  
**Kind**: init

Creates a linguistic tagger instance using the specified tag schemes and options.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(tagSchemes: [NSLinguisticTagScheme], options opts: Int)
```

#### Return Value

An initialized linguistic tagger.

#### Discussion

Pass any tag schemes to `tagSchemes` that you intend to use with the methods described in Enumerating Linguistic Tags and Getting Linguistic Tags.

> 💡 **Tip**:  Avoid specifying tag schemes that you won’t use to ensure optimal performance.

 Avoid specifying tag schemes that you won’t use to ensure optimal performance.

## Parameters

- `tagSchemes`: An array of tag schemes to be used. See   for the possible values.
- `opts`: Reserved for future use. Specify   for this parameter.

## See Also

- [struct NSLinguisticTagScheme](nslinguistictagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.
- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md)
  Enumerate the words in a string.
- [var string: String?](nslinguistictagger/string.md)
  The string being analyzed by the linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/init(tagschemes:options:))*