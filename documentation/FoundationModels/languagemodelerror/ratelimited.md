# LanguageModelError.RateLimited

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

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
- [init(resetDate: Date?, debugDescription: String, metadata: [String : any Sendable])](./ratelimited/init%28resetdate,debugdescription,metadata%29.md)
  Creates information describing a rate-limiting event.
### Inspecting rate-limit errors
- [var metadata: [String : any Sendable]](./ratelimited/metadata.md)
  Additional information about the failure, keyed by name.
- [var resetDate: Date?](./ratelimited/resetdate.md)
  The date after which retrying is likely to succeed, if known.
- [var debugDescription: String](./ratelimited/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Session rate limited error
- [case rateLimited(LanguageModelError.RateLimited)](./ratelimited%28_%29.md)
  The session has been rate limited.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/ratelimited)*