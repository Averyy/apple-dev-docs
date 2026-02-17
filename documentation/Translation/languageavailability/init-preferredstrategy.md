# init(preferredStrategy:)

**Framework**: Translation  
**Kind**: init

Creates a language availability, specifying what the preferred strategy is.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
init(preferredStrategy: TranslationSession.Strategy)
```

#### Discussion

Use `.lowLatency` for latency-sensitive applications that require fast, power-efficient translation. Use `.highFidelity` for translations more fluent in the target language, broader language support and immediate availability on Apple Intelligence-enabled devices.

## See Also

- [init()](languageavailability/init.md)
  Creates a language availability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/init(preferredstrategy:))*