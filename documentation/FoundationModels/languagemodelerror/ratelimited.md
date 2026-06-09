# LanguageModelError.RateLimited

**Framework**: Foundation Models  
**Kind**: struct

Information about a rate limiting event.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct RateLimited
```

## Topics

### Creating an error instance
- [init(resetDate: Date?, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/ratelimited/init(resetdate:debugdescription:metadata:).md)
### Inspecting rate-limit errors
- [var metadata: [String : any Sendable]](languagemodelerror/ratelimited/metadata.md)
- [var resetDate: Date?](languagemodelerror/ratelimited/resetdate.md)
- [var debugDescription: String](languagemodelerror/ratelimited/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case rateLimited(LanguageModelError.RateLimited)](languagemodelerror/ratelimited(_:).md)
  The session has been rate limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/ratelimited)*