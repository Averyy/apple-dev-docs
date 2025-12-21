# CredentialSession.Credential.InstanceInfo

**Framework**: SecureElementCredential  
**Kind**: struct

Information about an applet instance associated with a specific credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
struct InstanceInfo
```

## Topics

### Inspecting instance identifiers
- [let instanceAID: Data](credentialsession/credential/instanceinfo/instanceaid.md)
  The unique identifier for the applet instance.
- [let packageAID: Data](credentialsession/credential/instanceinfo/packageaid.md)
  The unique identifier of the package you use to install the instance.
- [let moduleAID: Data](credentialsession/credential/instanceinfo/moduleaid.md)
  The module identifier of the package with which this instance is associated.
### Inspecting the instance type
- [let instanceType: CredentialSession.Credential.InstanceInfo.InstanceType](credentialsession/credential/instanceinfo/instancetype-swift.property.md)
  The instance type of this instance.
- [CredentialSession.Credential.InstanceInfo.InstanceType](credentialsession/credential/instanceinfo/instancetype-swift.enum.md)
  An enumeration of Secure Element applet instance types.
### Creating a secure channel
- [let securityDomainAID: Data](credentialsession/credential/instanceinfo/securitydomainaid.md)
  The unique identifier of the security domain you use to install the instance.
- [let securityDomainKeyInfo: Data](credentialsession/credential/instanceinfo/securitydomainkeyinfo.md)
  A data blob which contains the security domain On-Board Generated Key (OBGK).
### Inspecting applet instance state
- [let lifeCycleState: Data](credentialsession/credential/instanceinfo/lifecyclestate.md)
  Information about the state of the applet instance.
### Instance Properties
- [var securityDomainCounter: Int](credentialsession/credential/instanceinfo/securitydomaincounter.md)
  The authentication counter of the security domain. Fetches the latest counter from the remote hardware.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo)*