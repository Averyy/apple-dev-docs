# CredentialSession.Credential.State

**Framework**: SecureElementCredential  
**Kind**: enum  
**Role**: Enumeration

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
- [CredentialSession.Credential.State.installationPending](./state-swift.enum/installationpending.md)
  The credential installation is pending but isn’t complete.
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](./state-swift.enum/installed%28instances%29.md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.InstanceInfo](./instanceinfo.md)
  Information about an applet instance associated with a specific credential.
- [CredentialSession.Credential.State.installationFailed](./state-swift.enum/installationfailed.md)
  The credential installation failed.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Inspecting credential state
- [let state: CredentialSession.Credential.State](./state-swift.property.md)
  A snapshot of the credential’s installation state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum)*