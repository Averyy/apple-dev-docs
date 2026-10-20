# CredentialSession.Credential.InstanceInfo

**Framework**: SecureElementCredential  
**Kind**: struct  
**Role**: Structure

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
- [let instanceAID: Data](./instanceinfo/instanceaid.md)
  The unique identifier for the applet instance.
- [let packageAID: Data](./instanceinfo/packageaid.md)
  The unique identifier of the package you use to install the instance.
- [let moduleAID: Data](./instanceinfo/moduleaid.md)
  The module identifier of the package with which this instance is associated.
### Inspecting the instance type
- [let instanceType: CredentialSession.Credential.InstanceInfo.InstanceType](./instanceinfo/instancetype-swift.property.md)
  The instance type of this instance.
- [CredentialSession.Credential.InstanceInfo.InstanceType](./instanceinfo/instancetype-swift.enum.md)
  An enumeration of Secure Element applet instance types.
### Creating a secure channel
- [let securityDomainAID: Data](./instanceinfo/securitydomainaid.md)
  The unique identifier of the security domain you use to install the instance.
- [let securityDomainKeyInfo: Data](./instanceinfo/securitydomainkeyinfo.md)
  A data blob which contains the security domain On-Board Generated Key (OBGK).
### Inspecting applet instance state
- [let lifeCycleState: Data](./instanceinfo/lifecyclestate.md)
  Information about the state of the applet instance.
### Instance Properties
- [var securityDomainCounter: Int](./instanceinfo/securitydomaincounter.md)
  The authentication counter of the security domain.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo)*