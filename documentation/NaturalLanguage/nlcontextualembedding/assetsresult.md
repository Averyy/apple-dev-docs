# NLContextualEmbedding.AssetsResult

**Framework**: Natural Language  
**Kind**: enum

The availability of the contextual embedding model assets.

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

#### Overview

The framework downloads models over-the-air, so check asset availability and download them if needed.

```swift
if !embeddingModel.hasAvailableAssets {
    let downloadResult = try await embeddingModel.requestAssets()
    guard downloadResult == .available else {
       print("Assets are not available locally and failed to be downloaded. Check your network connection and try again later.")
       return
   }
}
```

## Topics

### Getting the result status
- [NLContextualEmbedding.AssetsResult.available](nlcontextualembedding/assetsresult/available.md)
  A result that indicates that the assets are present on-device.
- [NLContextualEmbedding.AssetsResult.notAvailable](nlcontextualembedding/assetsresult/notavailable.md)
  A result that indicates that the assets aren’t present on-device.
- [NLContextualEmbedding.AssetsResult.error](nlcontextualembedding/assetsresult/error.md)
  A result that indicates the framework encounters an error.
### Initializers
- [init?(rawValue: Int)](nlcontextualembedding/assetsresult/init(rawvalue:).md)
  Creates an embedding key with the given string as its raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func requestAssets(completionHandler: (NLContextualEmbedding.AssetsResult, (any Error)?) -> Void)](nlcontextualembedding/requestassets(completionhandler:).md)
  Requests embedding model assets and downloads them if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/assetsresult)*