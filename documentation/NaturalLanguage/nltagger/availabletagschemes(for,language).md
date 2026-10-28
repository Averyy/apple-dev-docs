# availableTagSchemes(for:language:)

**Framework**: Natural Language  
**Kind**: method  
**Role**: Type Method

Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.

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
class func availableTagSchemes(for unit: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]
```

```objc
+ (NSArray<NSString *> *) availableTagSchemesForUnit:(NLTokenUnit) unit language:(NLLanguage) language;
```

## Return Value

The supported tag schemes. For possible values, see [`NLTagScheme`](../nltagscheme.md).

## Parameters

- `unit`: The linguistic unit. For possible values, see [`NLTokenUnit`](../nltokenunit.md).
- `language`: The [`NLLanguage`](../nllanguage.md) identifying the language.

## See Also

### Getting the tag schemes
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](./requestassets%28for,tagscheme,completionhandler%29.md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](./assetsresult.md)
  The response to an asset request.
- [var tagSchemes: [NLTagScheme]](./tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](../nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/availabletagschemes(for:language:))*