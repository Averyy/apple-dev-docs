# securityDomainCounter

**Framework**: SecureElementCredential  
**Kind**: property

The authentication counter of the security domain.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+

## Declaration

```swift
var securityDomainCounter: Int { get async throws }
```

#### Discussion

Accessing this property fetches the latest counter from the remote hardware.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/securitydomaincounter)*