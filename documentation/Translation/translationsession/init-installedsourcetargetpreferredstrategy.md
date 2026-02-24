# init(installedSource:target:preferredStrategy:)

**Framework**: Translation  
**Kind**: init

Creates a translation session to translate between a given source and target language already installed on device.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.0+
- macOS 26.4+ (Beta)

## Declaration

```swift
convenience init(installedSource source: Locale.Language, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy)
```

#### Discussion

If one or both of the languages aren’t installed on the device already, attempting to translate will throw errors. In order to get the person’s permission to download languages that aren’t already installed, translate using a `TranslationSession` provided by [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) or [`translationTask(source:target:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:)) .

> **Note**: If you created `TranslationSession` using `TranslationSession/init(installedSource:target:model:)`,  you don’t need a `.translationTask()`, however, you will need a `sourceLanguage` .

## Parameters

- `preferredStrategy`: Specify the preferred translation strategy to use. If `.highFidelity` is specified, the framework can still fall back to the `.lowLatency` strategy in some cases, such as when Apple Intelligence isn’t available.

## See Also

- [convenience init(installedSource: Locale.Language, target: Locale.Language?)](translationsession/init(installedsource:target:).md)
  Creates a translation session to translate between a given source and target language already installed on device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:preferredstrategy:))*