# lowLatency

**Framework**: Translation  
**Kind**: property

A translation strategy that performs translations quickly and is suitable for uses requiring low-latency such as translating audio in real time. While this strategy may produce translations with less accuracy than the `.highFidelity` strategy, it still has good accuracy, and it translates faster and uses less power. Translating with this strategy needs each language to be downloaded by the user, but once downloaded those languages are available to all apps that need them. This is the only strategy available on devices that don’t support Apple Intelligence. This strategy might still be used when specifying `.highFidelity` in cases where Apple Intelligence isn’t available or disabled.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
static let lowLatency: TranslationSession.Strategy
```

#### Discussion

This is the default model for apps built before the iOS 26.4 and macOS 26.4 SDKs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy/lowlatency)*