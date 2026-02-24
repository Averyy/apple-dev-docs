# AccountMailSMIME_EncryptionObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for S/MIME encryption.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.1+

## Declaration

```swift
object AccountMailSMIME_EncryptionObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the system enables S/MIME encryption by default, which the user can’t override if `PerMessageSwitchEnabled` is `false`.
- `IdentityAssetReference` (string): Specifies the identifier of an asset declaration containing the identity required for S/MIME encryption. The system attaches the public certificate to outgoing mail to allow the user to receive encrypted mail. When the user sends encrypted mail, the system uses the public certificate to encrypt the copy of the mail in their Sent mailbox.
- `IdentityUserOverrideable` (boolean): If `true`, the user can select an S/MIME signing identity in Settings.
- `PerMessageSwitchEnabled` (boolean): If `true`, the system enables the per-message encryption switch in the compose view.
- `UserOverrideable` (boolean): If `true`, the user can set the default value for S/MIME encryption to on or off in Settings.

## See Also

- [object AccountMailSMIME_SigningObject](accountmailsmime_signingobject.md)
  Settings for S/MIME signing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountmailsmime_encryptionobject)*