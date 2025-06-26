# init(installedSource:target:)

**Framework**: Translation  
**Kind**: init

Creates a translation session to translate between a given source and target language already installed on device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
convenience init(installedSource source: Locale.Language, target: Locale.Language?)
```

#### Discussion

If one or both of the languages aren’t installed on the device already, attempting to translate will throw errors. In order to get the person’s permission to download languages that aren’t already installed, translate using a `TranslationSession` provided by [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:)) or [`translationTask(source:target:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:)) .

> **Note**: If you created `TranslationSession` using [`init(installedSource:target:)`](translationsession/init(installedsource:target:).md),  you don’t need a `.translationTask()`, however, you will need a `sourceLanguage` .


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:))*