# LanguageModelError.Timeout

**Framework**: Foundation Models  
**Kind**: struct

Information about a timeout.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Timeout
```

## Topics

### Creating an error instance
- [init(debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/timeout/init(debugdescription:metadata:).md)
  Creates information describing a request timeout.
### Inspecting timeout errors
- [var metadata: [String : any Sendable]](languagemodelerror/timeout/metadata.md)
  Additional information about the failure, keyed by name.
- [var debugDescription: String](languagemodelerror/timeout/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case timeout(LanguageModelError.Timeout)](languagemodelerror/timeout(_:).md)
  The request timed out before the model could produce a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/timeout)*