# availableTagSchemes(forLanguage:)

**Framework**: Foundation  
**Kind**: method

Returns the tag schemes available for a particular language on the current device.

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
class func availableTagSchemes(forLanguage language: String) -> [NSLinguisticTagScheme]
```

#### Return Value

The available tag schemes. For possible values, see [`NSLinguisticTagScheme`](nslinguistictagscheme.md).

#### Discussion

This is a convenience method for calling the [`availableTagSchemes(for:language:)`](nslinguistictagger/availabletagschemes(for:language:).md), passing [`NSLinguisticTaggerUnit.word`](nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `language`: A BCP-47 tag identifying the language. For example, “en” for English or  “zh-Hans” for Chinese written using the Simplified Chinese script.

## See Also

- [class func availableTagSchemes(for: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]](nslinguistictagger/availabletagschemes(for:language:).md)
  Returns the tag schemes available for a particular unit and language on the current device.
- [var tagSchemes: [NSLinguisticTagScheme]](nslinguistictagger/tagschemes.md)
  Returns the tag schemes configured for this linguistic tagger. For possible values, see [`NSLinguisticTagScheme`](nslinguistictagscheme.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/availabletagschemes(forlanguage:))*