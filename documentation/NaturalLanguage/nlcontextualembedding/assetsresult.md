# NLContextualEmbedding.AssetsResult

**Framework**: Natural Language  
**Kind**: enum

The status of an asset request.

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

### Getting the result status
- [NLContextualEmbedding.AssetsResult.available](nlcontextualembedding/assetsresult/available.md)
  A result that indicates assets are available.
- [NLContextualEmbedding.AssetsResult.notAvailable](nlcontextualembedding/assetsresult/notavailable.md)
  A result that indicates assets aren’t available.
- [NLContextualEmbedding.AssetsResult.error](nlcontextualembedding/assetsresult/error.md)
  A result that indicates the framework encounters an error.
### Initializers
- [init?(rawValue: Int)](nlcontextualembedding/assetsresult/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func requestAssets(completionHandler: (NLContextualEmbedding.AssetsResult, (any Error)?) -> Void)](nlcontextualembedding/requestassets(completionhandler:).md)
  Requests assets for an embedding, if available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/naturallanguage/nlcontextualembedding/assetsresult)*