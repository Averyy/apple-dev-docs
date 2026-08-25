# AccountExchangeSMIME_SigningObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for S/MIME signing. Applicable for “EAS” only.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.1+

## Declaration

```swift
object AccountExchangeSMIME_SigningObject
```

## Properties

- `Enabled` (boolean) *(required)*: If `true`, the system enables S/MIME signing. Applicable for “EAS” only.
- `IdentityAssetReference` (string): The identifier of an asset declaration containing the identity required for S/MIME signing of messages sent from this account. Applicable for “EAS” only.
- `IdentityUserOverrideable` (boolean): If `true`, the user can select an S/MIME signing identity in Settings. Applicable for “EAS” only.
- `UserOverrideable` (boolean): If `true`, the user can turn S/MIME signing on or off in Settings. Applicable for “EAS” only.

## See Also

- [object AccountExchangeSMIME_EncryptionObject](accountexchangesmime_encryptionobject.md)
  Settings for S/MIME encryption. Applicable for “EAS” only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/accountexchangesmime_signingobject)*