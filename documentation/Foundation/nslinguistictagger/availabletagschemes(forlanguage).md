# availableTagSchemes(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the tag schemes available for a particular language on the current device.

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
class func availableTagSchemes(forLanguage language: String) -> [NSLinguisticTagScheme]
```

```objc
+ (NSArray<NSString *> *) availableTagSchemesForLanguage:(NSString *) language;
```

#### Return Value

The available tag schemes. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).

#### Discussion

This is a convenience method for calling the [`availableTagSchemes(for:language:)`](./availabletagschemes%28for,language%29.md), passing [`NSLinguisticTaggerUnit.word`](../nslinguistictaggerunit/word.md) as the linguistic unit.

## Parameters

- `language`: A BCP-47 tag identifying the language. For example, “en” for English or  “zh-Hans” for Chinese written using the Simplified Chinese script.

## See Also

### Getting the Tag Schemes
- [class func availableTagSchemes(for: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]](./availabletagschemes%28for,language%29.md)
  Returns the tag schemes available for a particular unit and language on the current device.
- [var tagSchemes: [NSLinguisticTagScheme]](./tagschemes.md)
  Returns the tag schemes configured for this linguistic tagger. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/availabletagschemes(forlanguage:))*