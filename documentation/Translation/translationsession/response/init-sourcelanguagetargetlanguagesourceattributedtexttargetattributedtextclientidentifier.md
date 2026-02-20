# init(sourceLanguage:targetLanguage:sourceAttributedText:targetAttributedText:clientIdentifier:)

**Framework**: Translation  
**Kind**: init

Creates an instance of a translation response.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceAttributedText: AttributedString, targetAttributedText: AttributedString, clientIdentifier: String? = nil)
```

#### Discussion

You don’t normally use this initializer directly. Instead, let the translation functions create instances of this type for you. Use this initializer when you want to create sample response for a test, for example in a SwiftUI preview.

## See Also

- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceText: String, targetText: String, clientIdentifier: String?)](translationsession/response/init(sourcelanguage:targetlanguage:sourcetext:targettext:clientidentifier:).md)
  Creates an instance of a translation response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/init(sourcelanguage:targetlanguage:sourceattributedtext:targetattributedtext:clientidentifier:))*