# LanguageModelError.Timeout

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

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
- [init(debugDescription: String, metadata: [String : any Sendable])](./timeout/init%28debugdescription,metadata%29.md)
  Creates information describing a request timeout.
### Inspecting timeout errors
- [var metadata: [String : any Sendable]](./timeout/metadata.md)
  Additional information about the failure, keyed by name.
- [var debugDescription: String](./timeout/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Request timed out error
- [case timeout(LanguageModelError.Timeout)](./timeout%28_%29.md)
  The request timed out before the model could produce a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/timeout)*