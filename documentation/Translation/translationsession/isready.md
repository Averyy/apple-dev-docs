# isReady

**Framework**: Translation  
**Kind**: property

A boolean value that indicates whether the system has installed the source and target languages of the session and is ready to begin translation.

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

Use this property to check whether a translation is likely to succeed. In a session that can request downloads, it prompts the person to approve downloads if languages aren’t ready yet. In a session that can’t request downloads, it will throw an error if the person calls any functions when languages aren’t ready.

If languages aren’t installed, attach a [`translationTask(_:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(_:action:))  or a [`translationTask(source:target:action:)`](https://developer.apple.com/documentation/SwiftUI/View/translationTask(source:target:action:))  function to a SwiftUI View. Then, call either [`prepareTranslation()`](translationsession/preparetranslation().md) or one of the translate functions so the system prompts the person to approve the language downloads.

> **Note**: This value returns whether the languages are currently installed. The person or system can still delete the downloaded languages after calling this, so make sure you handle the appropriate errors when calling one of the translate functions.

## See Also

- [var canRequestDownloads: Bool](translationsession/canrequestdownloads.md)
  A boolean value that indicates whether a translation session can request language downloads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/isready)*