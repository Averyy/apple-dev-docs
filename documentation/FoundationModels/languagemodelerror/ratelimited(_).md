# LanguageModelError.rateLimited(_:)

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

The session has been rate limited.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case rateLimited(LanguageModelError.RateLimited)
```

#### Discussion

This failure can happen if you make too many requests in a short window. You can recover from this error by spacing your requests or reducing system load. The exact solution may be model dependent.

## See Also

### Session rate limited error
- [LanguageModelError.RateLimited](./ratelimited.md)
  Information about a rate limiting event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/ratelimited(_:))*