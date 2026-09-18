# LanguageModelError.RateLimited

**Framework**: Foundation Models  
**Kind**: struct

Information about a rate limiting event.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct RateLimited
```

## Topics

### Creating an error instance
- [init(resetDate: Date?, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/ratelimited/init(resetdate:debugdescription:metadata:).md)
  Creates information describing a rate-limiting event.
### Inspecting rate-limit errors
- [var metadata: [String : any Sendable]](languagemodelerror/ratelimited/metadata.md)
  Additional information about the failure, keyed by name.
- [var resetDate: Date?](languagemodelerror/ratelimited/resetdate.md)
  The date after which retrying is likely to succeed, if known.
- [var debugDescription: String](languagemodelerror/ratelimited/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case rateLimited(LanguageModelError.RateLimited)](languagemodelerror/ratelimited(_:).md)
  The session has been rate limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/ratelimited)*