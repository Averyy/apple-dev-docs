# ASCredentialIdentityStoreError

**Framework**: Authentication Services  
**Kind**: struct

A credential identity store error.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
struct ASCredentialIdentityStoreError
```

## Topics

### Error domain
- [let ASCredentialIdentityStoreErrorDomain: String](ascredentialidentitystoreerrordomain.md)
  The domain for a credential identity store error.
- [static var internalError: ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/internalerror.md)
  The operation failed due to an internal error.
- [static var storeBusy: ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/storebusy.md)
  The operation failed because the credential identity store is busy.
- [static var storeDisabled: ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/storedisabled.md)
  The operation failed because the credential identity store is disabled.
- [ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/code.md)
  Constants that represent credential identity store error codes.
### Type Properties
- [static var errorDomain: String](ascredentialidentitystoreerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let ASCredentialIdentityStoreErrorDomain: String](ascredentialidentitystoreerrordomain.md)
  The domain for a credential identity store error.
- [ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/code.md)
  Constants that represent credential identity store error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystoreerror)*