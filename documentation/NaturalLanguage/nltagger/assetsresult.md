# NLTagger.AssetsResult

**Framework**: Natural Language  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NLTaggerAssetsResult : NSInteger;
```

## Topics

### Asset request responses
- [NLTagger.AssetsResult.available](./assetsresult/available.md)
  The asset is now available and loaded onto the device.
- [NLTagger.AssetsResult.notAvailable](./assetsresult/notavailable.md)
  The asset is unavailable on the device.
- [NLTagger.AssetsResult.error](./assetsresult/error.md)
  The framework couldn’t load the asset due to an error.
### Initializers
- [init?(rawValue: Int)](./assetsresult/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting the tag schemes
- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](./availabletagschemes%28for,language%29.md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](./requestassets%28for,tagscheme,completionhandler%29.md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [var tagSchemes: [NLTagScheme]](./tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](../nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/assetsresult)*