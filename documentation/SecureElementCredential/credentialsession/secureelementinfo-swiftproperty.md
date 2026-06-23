# secureElementInfo

**Framework**: SecureElementCredential  
**Kind**: property

A property that provides information about the Secure Element hardware.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
var secureElementInfo: CredentialSession.SecureElementInfo { get async throws }
```

#### Discussion

You can use the certificate in the [`CredentialSession.SecureElementInfo`](credentialsession/secureelementinfo-swift.struct.md) to authenticate against the Certification Authority of the Secure Element hardware.

- The most common errors are: - [`CredentialSession.ErrorCode.featureUnavailable`](credentialsession/errorcode/featureunavailable.md): The Secure Element credential feature isn’t available on this platform.
- [`CredentialSession.ErrorCode.sessionInvalidated`](credentialsession/errorcode/sessioninvalidated.md): The credential session has been invalidated.

## See Also

- [CredentialSession.SecureElementInfo](credentialsession/secureelementinfo-swift.struct.md)
  A type that provides information about the Secure Element hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/secureelementinfo-swift.property)*