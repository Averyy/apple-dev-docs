# highFidelity

**Framework**: Translation  
**Kind**: property

A translation strategy that performs translation with higher fidelity and fluency in the target language. This strategy will only be used when Apple Intelligence is enabled on the device, but doesn’t require an extra download when Apple Intelligence is enabled. It also supports more languages. However this strategy can be slower to run than the `.lowLatency` strategy, and can use additional power. It’s best to check that this strategy works for your app before enabling it for users.

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

On devices that don’t support Apple Intelligence or have Apple Intelligence disabled, the framework might still use the `.lowLatency` strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/strategy/highfidelity)*