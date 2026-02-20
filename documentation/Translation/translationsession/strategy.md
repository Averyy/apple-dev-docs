# TranslationSession.Strategy

**Framework**: Translation  
**Kind**: struct

A type that describes what strategy you need when performing translation in your app. APIs that take in a `Strategy` are setting a preferred model type, not guaranteeing this will be used.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
struct Strategy
```

## Topics

### Choosing a translation strategy
- [static let highFidelity: TranslationSession.Strategy](translationsession/strategy/highfidelity.md)
  A translation strategy that performs translation with higher fidelity and fluency in the target language. This strategy will only be used when Apple Intelligence is enabled on the device, but doesn’t require an extra download when Apple Intelligence is enabled. It also supports more languages. However this strategy can be slower to run than the `.lowLatency` strategy, and can use additional power. It’s best to check that this strategy works for your app before enabling it for users.
- [static let lowLatency: TranslationSession.Strategy](translationsession/strategy/lowlatency.md)
  A translation strategy that performs translations quickly and is suitable for uses requiring low-latency such as translating audio in real time. While this strategy may produce translations with less accuracy than the `.highFidelity` strategy, it still has good accuracy, and it translates faster and uses less power. Translating with this strategy needs each language to be downloaded by the user, but once downloaded those languages are available to all apps that need them. This is the only strategy available on devices that don’t support Apple Intelligence. This strategy might still be used when specifying `.highFidelity` in cases where Apple Intelligence isn’t available or disabled.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy)*