# tagSchemes

**Framework**: Natural Language  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly) NSArray<NSString *> * tagSchemes;
```

## See Also

### Getting the tag schemes
- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](./availabletagschemes%28for,language%29.md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [class func requestAssets(for: NLLanguage, tagScheme: NLTagScheme, completionHandler: (NLTagger.AssetsResult, (any Error)?) -> Void)](./requestassets%28for,tagscheme,completionhandler%29.md)
  Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.
- [NLTagger.AssetsResult](./assetsresult.md)
  The response to an asset request.
- [struct NLTagScheme](../nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/tagschemes)*