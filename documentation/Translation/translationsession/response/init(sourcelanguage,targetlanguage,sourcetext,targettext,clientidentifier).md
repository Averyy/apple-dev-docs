# init(sourceLanguage:targetLanguage:sourceText:targetText:clientIdentifier:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates an instance of a translation response.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceText: String, targetText: String, clientIdentifier: String? = nil)
```

#### Discussion

You don’t normally use this initializer directly. Instead, let the translation functions create instances of this type for you. Use this initializer when you want to create sample response for a test, for example in a SwiftUI preview.

## See Also

### Initializing a response
- [init(sourceLanguage: Locale.Language, targetLanguage: Locale.Language, sourceAttributedText: AttributedString, targetAttributedText: AttributedString, clientIdentifier: String?)](./init%28sourcelanguage,targetlanguage,sourceattributedtext,targetattributedtext,clientidentifier%29.md)
  Creates an instance of a translation response with formatted text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/init(sourcelanguage:targetlanguage:sourcetext:targettext:clientidentifier:))*