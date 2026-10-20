# NLContextualEmbedding.AssetsResult

**Framework**: Natural Language  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum NLContextualEmbeddingAssetsResult : NSInteger;
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
- [NLContextualEmbedding.AssetsResult.available](./assetsresult/available.md)
  A result that indicates that the assets are present on-device.
- [NLContextualEmbedding.AssetsResult.notAvailable](./assetsresult/notavailable.md)
  A result that indicates that the assets aren’t present on-device.
- [NLContextualEmbedding.AssetsResult.error](./assetsresult/error.md)
  A result that indicates the framework encounters an error.
### Initializers
- [init?(rawValue: Int)](./assetsresult/init%28rawvalue%29.md)
  Creates an embedding key with the given string as its raw value.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Requesting assets
- [func requestAssets(completionHandler: (NLContextualEmbedding.AssetsResult, (any Error)?) -> Void)](./requestassets%28completionhandler%29.md)
  Requests embedding model assets and downloads them if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/assetsresult)*