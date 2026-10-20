# init(installedSource:target:preferredStrategy:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

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

If one or both languages aren’t installed on the device, attempting to translate will throw errors. To get the person’s permission to download languages that aren’t already installed, translate using a [`TranslationSession`](../translationsession.md) provided by [`translationTask(_:action:)`](../../SwiftUI/view/translationtask%28_,action%29.md) or [`translationTask(source:target:action:)`](../../SwiftUI/view/translationtask%28source,target,action%29.md).

> **Note**: If you created a `TranslationSession` using [`init(installedSource:target:)`](./init%28installedsource,target%29.md), you don’t need a `.translationTask()`; however, you will need a [`sourceLanguage`](./sourcelanguage.md).

## Parameters

- `preferredStrategy`: The translation approach to use. [`highFidelity`](./strategy/highfidelity.md) uses Apple Intelligence models when available on device, or falls back to [`lowLatency`](./strategy/lowlatency.md) when those models aren’t available. The `lowLatency` strategy uses traditional models for translation.

## See Also

### Initalizing a translation session
- [convenience init(installedSource: Locale.Language, target: Locale.Language?)](./init%28installedsource,target%29.md)
  Creates a translation session to translate between a given source and target language already installed on device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:preferredstrategy:))*