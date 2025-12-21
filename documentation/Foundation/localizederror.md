# LocalizedError

**Framework**: Foundation  
**Kind**: protocol

A specialized error that provides localized messages describing the error and why it occurred.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol LocalizedError : Error
```

## Topics

### Instance Properties
- [var errorDescription: String?](localizederror/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](localizederror/failurereason.md)
  A localized message describing the reason for the failure.
- [var helpAnchor: String?](localizederror/helpanchor.md)
  A localized message providing “help” text if the user requests help.
- [var recoverySuggestion: String?](localizederror/recoverysuggestion.md)
  A localized message describing how one might recover from the failure.

## Relationships

### Inherits From
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [protocol Error](../Swift/Error.md)
  A type representing an error value that can be thrown.
- [class NSError](nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol RecoverableError](recoverableerror.md)
  A specialized error that may be recoverable by presenting several potential recovery options to the user.
- [protocol CustomNSError](customnserror.md)
  A specialized error that provides a domain, error code, and user-info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizederror)*