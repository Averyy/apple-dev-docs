# CredentialSession.Credential.State

**Framework**: SecureElementCredential  
**Kind**: enum

An enumeration of possible values of a credential’s installation state.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
enum State
```

## Topics

### Credential states
- [CredentialSession.Credential.State.installationPending](credentialsession/credential/state-swift.enum/installationpending.md)
  The credential installation is pending but isn’t complete.
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](credentialsession/credential/state-swift.enum/installed(instances:).md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.InstanceInfo](credentialsession/credential/instanceinfo.md)
  Information about an applet instance associated with a specific credential.
- [CredentialSession.Credential.State.installationFailed](credentialsession/credential/state-swift.enum/installationfailed.md)
  The credential installation failed.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let state: CredentialSession.Credential.State](credentialsession/credential/state-swift.property.md)
  A snapshot of the credential’s installation state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum)*