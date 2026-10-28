# init(sourceText:clientIdentifier:)

**Framework**: Translation  
**Kind**: init  
**Role**: Initializer

Creates a request for translating a single attributed string.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+
- macOS 26.4+

## Declaration

```swift
init(sourceText: AttributedString, clientIdentifier: String? = nil)
```

## Discussion

The plain text is automatically extracted and stored in [`sourceText`](./sourcetext.md).

## See Also

### Initializing a translation request
- [init(sourceText: String, clientIdentifier: String?)](./init%28sourcetext,clientidentifier%29-ruyz.md)
  Creates a request for translating a single string of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/request/init(sourcetext:clientidentifier:)-8fung)*