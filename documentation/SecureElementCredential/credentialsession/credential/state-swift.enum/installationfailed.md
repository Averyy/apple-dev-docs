# CredentialSession.Credential.State.installationFailed

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The credential installation failed.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case installationFailed
```

## Discussion

A credential is only in this state following a failed installation. Prior to success or failure, the state is [`CredentialSession.Credential.State.installationPending`](./installationpending.md).

## See Also

### Credential states
- [CredentialSession.Credential.State.installationPending](./installationpending.md)
  The credential installation is pending but isn’t complete.
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](./installed%28instances%29.md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.InstanceInfo](../instanceinfo.md)
  Information about an applet instance associated with a specific credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum/installationfailed)*