# preferredStrategy

**Framework**: Translation  
**Kind**: property

The preferred strategy of translation to check availability for.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
var preferredStrategy: TranslationSession.Strategy { get }
```

#### Discussion

Set this property to determine which translation models the framework considers when checking language availability. [`lowLatency`](translationsession/strategy/lowlatency.md) checks for traditional translation models that work on all devices. [`highFidelity`](translationsession/strategy/highfidelity.md) checks for Apple Intelligence models that provide more fluent translations. When Apple Intelligence is enabled, these models are already downloaded, so translation is immediately available without prompting the person to download languages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/languageavailability/preferredstrategy)*