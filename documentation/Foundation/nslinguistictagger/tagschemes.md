# tagSchemes

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns the tag schemes configured for this linguistic tagger. For possible values, see [`NSLinguisticTagScheme`](../nslinguistictagscheme.md).

**Availability**:
- iOS 5.0+ - Deprecated in 27.3
- iPadOS 5.0+ - Deprecated in 27.3
- Mac Catalyst 13.1+ - Deprecated in 27.3
- macOS 10.7+ - Deprecated in 27.3
- tvOS 9.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 2.0+ - Deprecated in 27.3

> **Deprecated**: All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

## Declaration

```swift
var tagSchemes: [NSLinguisticTagScheme] { get }
```

```objc
@property (copy, readonly) NSArray<NSString *> * tagSchemes;
```

## See Also

### Getting the Tag Schemes
- [class func availableTagSchemes(for: NSLinguisticTaggerUnit, language: String) -> [NSLinguisticTagScheme]](./availabletagschemes%28for,language%29.md)
  Returns the tag schemes available for a particular unit and language on the current device.
- [class func availableTagSchemes(forLanguage: String) -> [NSLinguisticTagScheme]](./availabletagschemes%28forlanguage%29.md)
  Returns the tag schemes available for a particular language on the current device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslinguistictagger/tagschemes)*