# tagSchemes

**Framework**: Natural Language  
**Kind**: property

The tag schemes configured for this linguistic tagger.

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
var tagSchemes: [NLTagScheme] { get }
```

## See Also

- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](nltagger/availabletagschemes(for:language:).md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](nltagger/requestassets(for:tagscheme:completionhandler:).md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](nltagger/assetsresult.md)
  The response to an asset request.
- [struct NLTagScheme](nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tagschemes)*