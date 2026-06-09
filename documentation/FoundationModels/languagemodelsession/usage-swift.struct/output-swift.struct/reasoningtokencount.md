# reasoningTokenCount

**Framework**: Foundation Models  
**Kind**: property

The number of output tokens that were part of the model’s reasoning output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
var reasoningTokenCount: Int
```

#### Discussion

This value will always be less than or equal to [`totalTokenCount`](languagemodelsession/usage-swift.struct/output-swift.struct/totaltokencount.md). A non-zero value requires the model to declare the [`reasoning`](languagemodelcapabilities/capability/reasoning.md) capability.

## See Also

- [var totalTokenCount: Int](languagemodelsession/usage-swift.struct/output-swift.struct/totaltokencount.md)
  The total number of output tokens.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelsession/usage-swift.struct/output-swift.struct/reasoningtokencount)*