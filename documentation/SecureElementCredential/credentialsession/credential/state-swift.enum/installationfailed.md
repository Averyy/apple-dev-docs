# CredentialSession.Credential.State.installationFailed

**Framework**: SecureElementCredential  
**Kind**: case

The credential installation failed.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case installationFailed
```

#### Discussion

A credential is only in this state following a failed installation. Prior to success or failure, the state is [`CredentialSession.Credential.State.installationPending`](credentialsession/credential/state-swift.enum/installationpending.md).

## See Also

- [CredentialSession.Credential.State.installationPending](credentialsession/credential/state-swift.enum/installationpending.md)
  The credential installation is pending but isn’t complete.
- [case installed(instances: [CredentialSession.Credential.InstanceInfo])](credentialsession/credential/state-swift.enum/installed(instances:).md)
  The credential installation is complete for one or more instances.
- [CredentialSession.Credential.InstanceInfo](credentialsession/credential/instanceinfo.md)
  Information about an applet instance associated with a specific credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum/installationfailed)*