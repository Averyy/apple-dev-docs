# init(sourceLanguage:targetLanguage:sourceAttributedText:targetAttributedText:clientIdentifier:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates an instance of a translation response with formatted text.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceAttributedText: AttributedString, targetAttributedText: AttributedString, clientIdentifier: String? = nil)
```

#### Discussion

You don’t normally use this initializer directly. Instead, let the translation functions create instances of this type for you. Use this initializer when you want to create sample response for a test, for example in a SwiftUI preview.

## See Also

### Initializing a response
- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceText: String, targetText: String, clientIdentifier: String?)](./init%28sourcelanguage,targetlanguage,sourcetext,targettext,clientidentifier%29.md)
  Creates an instance of a translation response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/init(sourcelanguage:targetlanguage:sourceattributedtext:targetattributedtext:clientidentifier:))*