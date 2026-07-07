# securityDomainCounter

**Framework**: SecureElementCredential  
**Kind**: property

The authentication counter of the security domain.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
var securityDomainCounter: Int { get async throws }
```

#### Discussion

Accessing this property fetches the latest counter from the remote hardware.

- The most common errors are: - [`CredentialSession.ErrorCode.resourceUnavailable`](credentialsession/errorcode/resourceunavailable.md): The system service is temporarily unavailable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/securitydomaincounter)*