# securityDomainKeyInfo

**Framework**: SecureElementCredential  
**Kind**: property

A data blob which contains the security domain On-Board Generated Key (OBGK).

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let securityDomainKeyInfo: Data
```

#### Discussion

This data has the information required to form a Secure Channel Protocol 3 (SCP03) channel between the user and the security domain.

## See Also

- [let securityDomainAID: Data](credentialsession/credential/instanceinfo/securitydomainaid.md)
  The unique identifier of the security domain you use to install the instance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/securitydomainkeyinfo)*