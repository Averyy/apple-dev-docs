# clientIdentifier

**Framework**: Translation  
**Kind**: property

The unique identifier matching the client identifier set in the translation request.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
let clientIdentifier: String?
```

#### Discussion

Use this identifier to associate a translation request with its response. If you set a client identifier in the translation request, that same identifier returns in the response. If the request contained no identifier, this value is `nil`.

## See Also

- [let sourceLanguage: Locale.Language](translationsession/response/sourcelanguage.md)
  The language that the framework translated the text from.
- [let targetLanguage: Locale.Language](translationsession/response/targetlanguage.md)
  The language that the framework translated the text into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/response/clientidentifier)*