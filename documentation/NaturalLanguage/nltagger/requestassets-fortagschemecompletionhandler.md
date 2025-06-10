# requestAssets(for:tagScheme:completionHandler:)

**Framework**: Natural Language  
**Kind**: method

Asks the Natural Language framework to load any missing assets for a tag scheme onto the device for the given language.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func requestAssets(for language: NLLanguage, tagScheme: NLTagScheme) async throws -> NLTagger.AssetsResult
```

#### Discussion

> ❗ **Important**:  You can call this method from synchronous code using a completion handler, as shown on this page, or you can call it as an asynchronous method that has the following declaration: ```swift
class func requestAssets(for language: NLLanguage, tagScheme: NLTagScheme) async throws -> NLTagger.AssetsResult
``` For information about concurrency and asynchronous code in Swift, see [`Calling Objective-C APIs Asynchronously`](https://developer.apple.com/documentation/Swift/calling-objective-c-apis-asynchronously).

Before using this method, use [`availableTagSchemes(for:language:)`](nltagger/availabletagschemes(for:language:).md) to check whether a tag scheme is available on the device. When a tag scheme is unavailable for a specific language, it may be because the framework hasn’t loaded the support for that language.

Use this method to ask the [`Natural Language`](NaturalLanguage.md) framework to load any missing assets for that tag scheme. This method returns immediately but the framework may need time to complete the request. When the framework completes the request, it notifies your app with the `completionHandler` you provided to the method. In your completion handler, use the `result` parameter to check whether the tag scheme is now available.

The [`Natural Language`](NaturalLanguage.md) framework may call your `completionHandler` immediately if it knows the state of the tag scheme’s assets or if it experiences an error.

## Parameters

- `language`: The language of the tag scheme that you’re asking the framework to load onto the device.
- `tagScheme`: The tag scheme that you’re asking the framework to load onto the device.
- `completionHandler`: A closure the framework uses to notify your app when the tag scheme request has completed.

## See Also

- [class func availableTagSchemes(for: NLTokenUnit, language: NLLanguage) -> [NLTagScheme]](nltagger/availabletagschemes(for:language:).md)
  Retrieves the tag schemes available for a particular unit (like word or sentence) and language on the current device.
- [NLTagger.AssetsResult](nltagger/assetsresult.md)
  The response to an asset request.
- [var tagSchemes: [NLTagScheme]](nltagger/tagschemes.md)
  The tag schemes configured for this linguistic tagger.
- [struct NLTagScheme](nltagscheme.md)
  Constants for the tag schemes specified when initializing a linguistic tagger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nltagger/requestassets(for:tagscheme:completionhandler:))*