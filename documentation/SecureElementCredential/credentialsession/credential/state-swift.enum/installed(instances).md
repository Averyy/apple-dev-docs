# CredentialSession.Credential.State.installed(instances:)

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The credential installation is complete for one or more instances.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case installed(instances: [CredentialSession.Credential.InstanceInfo])
```

## Discussion

The associated value `instances` is an array of applet instances associated with the installed credential.

## See Also

### Credential states
- [CredentialSession.Credential.State.installationPending](./installationpending.md)
  The credential installation is pending but isn’t complete.
- [CredentialSession.Credential.InstanceInfo](../instanceinfo.md)
  Information about an applet instance associated with a specific credential.
- [CredentialSession.Credential.State.installationFailed](./installationfailed.md)
  The credential installation failed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/credential/state-swift.enum/installed(instances:))*