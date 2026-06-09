# LanguageModelError.ContextSizeExceeded

**Framework**: Foundation Models  
**Kind**: struct

Information about exceeding the context window size.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct ContextSizeExceeded
```

## Topics

### Creating an error instance
- [init(contextSize: Int, tokenCount: Int, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/contextsizeexceeded/init(contextsize:tokencount:debugdescription:metadata:).md)
### Inspecting context size errors
- [var metadata: [String : any Sendable]](languagemodelerror/contextsizeexceeded/metadata.md)
- [var tokenCount: Int](languagemodelerror/contextsizeexceeded/tokencount.md)
- [var contextSize: Int](languagemodelerror/contextsizeexceeded/contextsize.md)
- [var debugDescription: String](languagemodelerror/contextsizeexceeded/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case contextSizeExceeded(LanguageModelError.ContextSizeExceeded)](languagemodelerror/contextsizeexceeded(_:).md)
  The session’s transcript exceeded the model’s context size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/contextsizeexceeded)*