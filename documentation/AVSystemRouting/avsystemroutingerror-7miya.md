# AVSystemRoutingError

**Framework**: AVSystemRouting  
**Kind**: struct

An error that an AVSystemRouting operation throws when it fails.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
struct AVSystemRoutingError
```

## Topics

### Initializers
- [init(AVSystemRoutingError.Code)](avsystemroutingerror-7miya/init(_:).md)
  Creates an error with the specified error code.
### Instance Properties
- [let code: AVSystemRoutingError.Code](avsystemroutingerror-7miya/code-swift.property.md)
  The code that identifies the type of routing error.
- [var errorDescription: String?](avsystemroutingerror-7miya/errordescription.md)
  A localized description of the error.
- [var failureReason: String?](avsystemroutingerror-7miya/failurereason.md)
  A localized explanation of the reason for the error.
- [var helpAnchor: String?](avsystemroutingerror-7miya/helpanchor.md)
  A localized help anchor for the error.
- [var recoverySuggestion: String?](avsystemroutingerror-7miya/recoverysuggestion.md)
  A localized suggestion for how to recover from the error.
### Enumerations
- [AVSystemRoutingError.Code](avsystemroutingerror-7miya/code-swift.enum.md)
  The codes that identify the type of a routing error.

## Relationships

### Conforms To
- [Error](../swift/error.md)
- [LocalizedError](../foundation/localizederror.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AVSystemRoutingError](avsystemroutingerror-19zkj.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avsystemrouting/avsystemroutingerror-7miya)*