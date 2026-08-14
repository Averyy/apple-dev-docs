# LanguageModelError.Timeout

**Framework**: Foundation Models  
**Kind**: struct

Information about a timeout.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Timeout
```

## Topics

### Creating an error instance
- [init(debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/timeout/init(debugdescription:metadata:).md)
### Inspecting timeout errors
- [var metadata: [String : any Sendable]](languagemodelerror/timeout/metadata.md)
- [var debugDescription: String](languagemodelerror/timeout/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case timeout(LanguageModelError.Timeout)](languagemodelerror/timeout(_:).md)
  The request timed out before the model could produce a response.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/timeout)*