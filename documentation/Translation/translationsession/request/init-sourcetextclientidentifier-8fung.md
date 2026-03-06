# init(sourceText:clientIdentifier:)

**Framework**: Translation  
**Kind**: init

Creates a request for translating a single attributed string.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)
- macOS 26.4+ (Beta)

## Declaration

```swift
init(sourceText: AttributedString, clientIdentifier: String? = nil)
```

#### Discussion

The plain text is automatically extracted and stored in [`sourceText`](translationsession/request/sourcetext.md).

## See Also

- [init(sourceText: String, clientIdentifier: String?)](translationsession/request/init(sourcetext:clientidentifier:)-ruyz.md)
  Creates a request for translating a single string of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/request/init(sourcetext:clientidentifier:)-8fung)*