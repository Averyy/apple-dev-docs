# availableTagSchemes(for:language:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the tag schemes available for a particular unit and language on the current device.

**Availability**:
- iOS 11.0+ - Deprecated in 27.2
- iPadOS 11.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.2
- macOS 10.13+ - Deprecated in 27.2
- tvOS 11.0+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 4.0+ - Deprecated in 27.2

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
class func availableTagSchemes(for unit: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]
```

```objc
+ (NSArray<NSString *> *) availableTagSchemesForUnit:(NSLinguisticTaggerUnit) unit language:(NSString *) language;
```

## Return Value

The supported tag schemes. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).

## Parameters

- `unit`: The linguistic unit. For possible values, see [`NSLinguisticTaggerUnit`](../nslinguistictaggerunit.md).
- `language`: A BCP-47 tag identifying the language. For example, “en” for English or  “zh-Hans” for Chinese written using the Simplified Chinese script.

## See Also

### Getting the Tag Schemes
- [class func availableTagSchemes(forLanguage: String) -> [NSLinguisticTagScheme]](./availabletagschemes%28forlanguage%29.md)
  Returns the tag schemes available for a particular language on the current device.
- [var tagSchemes: [NSLinguisticTagScheme]](./tagschemes.md)
  Returns the tag schemes configured for this linguistic tagger. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/availabletagschemes(for:language:))*