# init(installedSource:target:)

**Framework**: Translation  
**Kind**: init

Create a `TranslationSession` to translate between a given source and target language already installed on the device.

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

If one or both languages aren’t installed on the device already, attempting to translate will throw errors. In order to get the user’s permission to download languages that aren’t already installed, translate using a `TranslationSession` provided by `View/translationTask(_:action:)` or `View/translationTask(source:target:action:)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/init(installedsource:target:))*