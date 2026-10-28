# secureElementInfo

**Framework**: SecureElementCredential  
**Kind**: property  
**Role**: Instance Property

A property that provides information about the Secure Element hardware.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
var secureElementInfo: CredentialSession.SecureElementInfo { get async throws }
```

## Discussion

You can use the certificate in the [`CredentialSession.SecureElementInfo`](./secureelementinfo-swift.struct.md) to authenticate against the Certification Authority of the Secure Element hardware.

- The most common errors are:

  - [`CredentialSession.ErrorCode.featureUnavailable`](./errorcode/featureunavailable.md): The Secure Element credential feature isn’t available on this platform.
  - [`CredentialSession.ErrorCode.sessionInvalidated`](./errorcode/sessioninvalidated.md): The credential session has been invalidated.

## See Also

### Accessing hardware information
- [CredentialSession.SecureElementInfo](./secureelementinfo-swift.struct.md)
  A type that provides information about the Secure Element hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.property)*