# cachedTokenCount

**Framework**: Foundation Models  
**Kind**: property

The number of input tokens that were served from a cache.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var cachedTokenCount: Int
```

#### Discussion

This value will always be less than or equal to [`totalTokenCount`](languagemodelsession/usage-swift.struct/input-swift.struct/totaltokencount.md).

## See Also

- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/input-swift.struct/totaltokencount.md)
  The total number of input tokens from the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/input-swift.struct/cachedtokencount)*