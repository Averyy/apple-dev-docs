# NLTagger.AssetsResult

**Framework**: Natural Language  
**Kind**: enum

The response to an asset request.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.0+
- macOS 10.14+
- tvOS 12.0+
- visionOS 1.0+
- watchOS 5.0+

## Declaration

```swift
enum AssetsResult
```

## Topics

### Asset request responses
- [NLTagger.AssetsResult.available](nltagger/assetsresult/available.md)
  The asset is now available and loaded onto the device.
- [NLTagger.AssetsResult.notAvailable](nltagger/assetsresult/notavailable.md)
  The asset is unavailable on the device.
- [NLTagger.AssetsResult.error](nltagger/assetsresult/error.md)
  The framework couldn’t load the asset due to an error.
### Initializers
- [init?(rawValue: Int)](nltagger/assetsresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](nltagger/availabletagschemes(for:language:).md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](nltagger/requestassets(for:tagscheme:completionhandler:).md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [var tagSchemes: [NLTagScheme]](nltagger/tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/assetsresult)*