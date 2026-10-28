# CredentialSession.Credential.State.installationPending

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The credential installation is pending but isn’t complete.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case installationPending
```

## Discussion

A credential is in this state after sending the provisioning request but before installation actually completes or fails.

## See Also

### Credential states
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](./installed%28instances%29.md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.InstanceInfo](../instanceinfo.md)
  Information about an applet instance associated with a specific credential.
- [CredentialSession.Credential.State.installationFailed](./installationfailed.md)
  The credential installation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum/installationpending)*