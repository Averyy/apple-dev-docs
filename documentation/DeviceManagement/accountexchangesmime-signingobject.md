# AccountExchangeSMIME_SigningObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for S/MIME signing.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.1+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object AccountExchangeSMIME_SigningObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the system enables S/MIME signing.
- `IdentityAssetReference` (string): Specifies the identifier of an asset declaration containing the identity required for S/MIME signing of messages sent from this account.
- `IdentityUserOverrideable` (boolean): If `true`, the user can select an S/MIME signing identity in Settings.
- `UserOverrideable` (boolean): If `true`, the user can turn S/MIME signing on or off in Settings.

## See Also

- [object AccountExchangeSMIME_EncryptionObject](accountexchangesmime_encryptionobject.md)
  Settings for S/MIME encryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountexchangesmime_signingobject)*