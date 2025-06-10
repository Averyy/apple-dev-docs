# isReady

**Framework**: Translation  
**Kind**: property

Whether the source and target languages of this session are installed and ready for translation.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
var isReady: Bool { get async }
```

#### Discussion

Use this function to determine whether the language assets the device requires for translating from the session’s source language to target language are downloaded.

Checking this property before using the session is recommended but optional. In a session that can request downloads, the user will see UI to approve downloads when translating if languages aren’t ready. Calling any functions when languages aren’t ready will result in errors if the session can’t request downloads.

If languages aren’t installed, attach a `View/translationTask(_:action:)` or `View/translationTask(source:target:action:)` function to a SwiftUI View, and call [`prepareTranslation()`](translationsession/preparetranslation().md) to get user approval to download the languages.

> **Note**: This value returns whether the languages are currently installed. The downloaded languages can still be deleted by the user or system after calling this, so make sure you handle the appropriate errors when calling one of the translate functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/isready)*