# cachedTokenCount

**Framework**: Foundation Models  
**Kind**: property

The number of input tokens that were served from a cache.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
var cachedTokenCount: Int
```

#### Discussion

This value is always less than or equal to [`totalTokenCount`](languagemodelsession/usage-swift.struct/input-swift.struct/totaltokencount.md).

## See Also

- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/input-swift.struct/totaltokencount.md)
  The total number of input tokens from the transcript.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/input-swift.struct/cachedtokencount)*