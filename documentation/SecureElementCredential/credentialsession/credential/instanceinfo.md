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
### Creating a secure channel
- [let securityDomainAID: Data](credentialsession/credential/instanceinfo/securitydomainaid.md)
  The unique identifier of the security domain you use to install the instance.
- [let securityDomainKeyInfo: Data](credentialsession/credential/instanceinfo/securitydomainkeyinfo.md)
  A data blob which contains the security domain On-Board Generated Key (OBGK).
### Inspecting applet instance state
- [let lifeCycleState: Data](credentialsession/credential/instanceinfo/lifecyclestate.md)
  Information about the state of the applet instance.
### Operators
- [static func == (CredentialSession.Credential.InstanceInfo, CredentialSession.Credential.InstanceInfo) -> Bool](credentialsession/credential/instanceinfo/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Instance Properties
- [var securityDomainCounter: Int](credentialsession/credential/instanceinfo/securitydomaincounter.md)
  The authentication counter of the security domain. Fetches the latest counter from the remote hardware.
### Default Implementations
- [Equatable Implementations](credentialsession/credential/instanceinfo/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [CredentialSession.Credential.State.installationPending](credentialsession/credential/state-swift.enum/installationpending.md)
  The credential installation is pending but isn’t complete.
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](credentialsession/credential/state-swift.enum/installed(instances:).md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.State.installationFailed](credentialsession/credential/state-swift.enum/installationfailed.md)
  The credential installation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/instanceinfo)*