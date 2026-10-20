# securityDomainAID

**Framework**: SecureElementCredential  
**Kind**: property  
**Role**: Instance Property

The unique identifier of the security domain you use to install the instance.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
let securityDomainAID: Data
```

#### Discussion

Use this identifier when selecting the security domain to perform data transceive with, such as forming a Secure Channel Protocol 3 (SCP03) channel.

## See Also

### Creating a secure channel
- [let securityDomainKeyInfo: Data](./securitydomainkeyinfo.md)
  A data blob which contains the security domain On-Board Generated Key (OBGK).


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo/securitydomainaid)*