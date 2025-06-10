# init(tagSchemes:)

**Framework**: Natural Language  
**Kind**: init

Creates a linguistic tagger instance using the specified tag schemes and options.

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
init(tagSchemes: [NLTagScheme])
```

#### Discussion

Pass any tag schemes to tagSchemes that you intend to use with the methods described in Enumerating linguistic tags and Getting linguistic tags in [`NLTagger`](nltagger.md).

> 💡 **Tip**:  Avoid specifying tag schemes that you won’t use to ensure optimal performance.

## Parameters

- `tagSchemes`: An array of tag schemes to be used. See   for the possible values.

## See Also

- [var string: String?](nltagger/string.md)
  The string being analyzed by the linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/init(tagschemes:))*