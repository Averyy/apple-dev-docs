# AAAttributionError

**Framework**: AdServices  
**Kind**: struct

The error code that the parent class issues.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Declaration

```swift
struct AAAttributionError
```

## Topics

### Error domain
- [static var errorDomain: String](aaattributionerror/errordomain.md)
  The error domain the framework uses when returning errors.
### Error codes
- [static var internalError: AAAttributionError.Code](aaattributionerror/internalerror.md)
  The server is unable to provide a token because of an internal error.
- [static var networkError: AAAttributionError.Code](aaattributionerror/networkerror.md)
  The server is unable to provide a token because the internet isn’t available.
- [static var platformNotSupported: AAAttributionError.Code](aaattributionerror/platformnotsupported.md)
  The server is unable to provide a token because of an unsupported operating system.
- [AAAttributionError.Code](aaattributionerror/code.md)
  The error code that the parent class issues.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let AAAttributionErrorDomain: String](aaattributionerrordomain.md)
  The framework attribution error domain.
- [AAAttributionError.Code](aaattributionerror/code.md)
  The error code that the parent class issues.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattributionerror)*