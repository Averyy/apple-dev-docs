# storeBusy

**Framework**: Authentication Services  
**Kind**: property

The operation failed because the credential identity store is busy.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static var storeBusy: ASCredentialIdentityStoreError.Code { get }
```

#### Discussion

Attempt the operation again at a later time.

## See Also

- [let ASCredentialIdentityStoreErrorDomain: String](ascredentialidentitystoreerrordomain.md)
  The domain for a credential identity store error.
- [static var internalError: ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/internalerror.md)
  The operation failed due to an internal error.
- [static var storeDisabled: ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/storedisabled.md)
  The operation failed because the credential identity store is disabled.
- [ASCredentialIdentityStoreError.Code](ascredentialidentitystoreerror/code.md)
  Constants that represent credential identity store error codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialidentitystoreerror/storebusy)*