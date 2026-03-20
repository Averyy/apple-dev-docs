# init(installedSource:target:preferredStrategy:)

**Framework**: Translation  
**Kind**: init

Creates a translation session to translate between a given source and target language already installed on device.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.0+
- macOS 26.4+

## Declaration

```swift
convenience init(installedSource source: Locale.Language, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy)
```

#### Discussion

If one or both languages aren’t installed on the device, attempting to translate will throw errors. To get the person’s permission to download languages that aren’t already installed, translate using a [`TranslationSession`](translationsession.md) provided by [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) or [`translationTask(source:target:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:)) .

> **Note**: If you created `TranslationSession` using [`init(installedSource:target:)`](translationsession/init(installedsource:target:).md), you don’t need a `.translationTask()`; however, you will need a [`sourceLanguage`](translationsession/sourcelanguage.md) .

## Parameters

- `preferredStrategy`: The translation approach to use. [`highFidelity`](translationsession/strategy/highfidelity.md) uses Apple Intelligence models when available on device, or falls back to [`lowLatency`](translationsession/strategy/lowlatency.md) when those models aren’t available. The `lowLatency` strategy uses traditional models for translation.

## See Also

- [convenience init(installedSource: Locale.Language, target: Locale.Language?)](translationsession/init(installedsource:target:).md)
  Creates a translation session to translate between a given source and target language already installed on device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:preferredstrategy:))*