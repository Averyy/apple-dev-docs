# init(installedSource:target:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates a translation session to translate between a given source and target language already installed on device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
convenience init(installedSource source: Locale.Language, target: Locale.Language?)
```

## Discussion

If one or both of the languages aren’t installed on the device already, attempting to translate will throw errors. In order to get the person’s permission to download languages that aren’t already installed, translate using a [`TranslationSession`](../translationsession.md) provided by [`translationTask(_:action:)`](../../SwiftUI/view/translationtask%28_,action%29.md) or [`translationTask(source:target:action:)`](../../SwiftUI/view/translationtask%28source,target,action%29.md).

> **Note**: If you created a `TranslationSession` using [`init(installedSource:target:)`](./init%28installedsource,target%29.md), you don’t need a `.translationTask()`; however, you will need a [`sourceLanguage`](./sourcelanguage.md).

## See Also

### Initalizing a translation session
- [convenience init(installedSource: Locale.Language, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy)](./init%28installedsource,target,preferredstrategy%29.md)
  Creates a translation session to translate between a given source and target language already installed on device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:))*