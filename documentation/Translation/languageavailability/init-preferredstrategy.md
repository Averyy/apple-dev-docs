# init(preferredStrategy:)

**Framework**: Translation  
**Kind**: init

Creates an instance for checking language availability with a preferred translation strategy.

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

Set this property to determine which translation models the framework considers when checking language availability. [`lowLatency`](translationsession/strategy/lowlatency.md) checks for traditional translation models that provide faster translations and use less power. [`highFidelity`](translationsession/strategy/highfidelity.md) checks for Apple Intelligence models that provide more fluent translations. When Apple Intelligence is enabled, these models are already downloaded, so translation is immediately available without prompting the person to download languages. On devices without Apple Intelligence, it falls back to the traditional models used by `lowLatency`.

## See Also

- [init()](languageavailability/init.md)
  Creates an instance to check what languages are available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/init(preferredstrategy:))*