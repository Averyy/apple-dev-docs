# highFidelity

**Framework**: Translation  
**Kind**: property

A translation strategy that provides more fluent translations using Apple Intelligence.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
static let highFidelity: TranslationSession.Strategy
```

#### Discussion

Use this strategy for higher-quality translations on devices with Apple Intelligence enabled. The models are already downloaded when Apple Intelligence is enabled, so no additional language downloads are required. This strategy offers higher-quality translations and supports additional languages, but may take longer to complete than [`lowLatency`](translationsession/strategy/lowlatency.md). On devices without Apple Intelligence, it falls back to the traditional models used by `lowLatency`.

## See Also

- [static let lowLatency: TranslationSession.Strategy](translationsession/strategy/lowlatency.md)
  A translation strategy that provides fast translations using traditional models.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy/highfidelity)*