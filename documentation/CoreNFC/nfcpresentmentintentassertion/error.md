# NFCPresentmentIntentAssertion.Error

**Framework**: Core NFC  
**Kind**: enum

An error type that indicates problems with the presentment intent assertion.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
enum Error
```

## Topics

### Presentment intent assertion errors
- [NFCPresentmentIntentAssertion.Error.systemEligibilityFailed](nfcpresentmentintentassertion/error/systemeligibilityfailed.md)
  The current system isn’t eligible to use this service.
- [NFCPresentmentIntentAssertion.Error.systemNotAvailable](nfcpresentmentintentassertion/error/systemnotavailable.md)
  The system is unavailable because it’s in the cool-down period.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var isValid: Bool](nfcpresentmentintentassertion/isvalid.md)
  A Boolean property that indicates whether the presentment intent assertion instance is still valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corenfc/nfcpresentmentintentassertion/error)*