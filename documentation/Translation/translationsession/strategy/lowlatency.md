# lowLatency

**Framework**: Translation  
**Kind**: property

A translation strategy that provides fast translations using traditional models.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.0+
- macOS 26.4+

## Declaration

```swift
static let lowLatency: TranslationSession.Strategy
```

#### Discussion

Use this strategy for scenarios that require low latency, such as translating audio in real time. This strategy requires downloading languages before use, but after they are downloaded they are available to all apps on the device. To download languages ahead of time, call [`prepareTranslation()`](translationsession/preparetranslation().md) before performing translations.

Compared to [`highFidelity`](translationsession/strategy/highfidelity.md), this strategy is faster and uses less power, though translations are not as fluent. This is the default strategy for devices without Apple Intelligence and apps built with SDKs before iOS 26.4 and macOS 26.4.

## See Also

- [static let highFidelity: TranslationSession.Strategy](translationsession/strategy/highfidelity.md)
  A translation strategy that provides more fluent translations using Apple Intelligence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy/lowlatency)*