# NetworkVPNIPSecAuthentication_XAuthObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control XAuth.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecAuthentication_XAuthObject
```

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (user name and password) required for XAuth. Required when `Enabled` key is set to `true`.
- `Enabled` (boolean) *(required)*: If `true`, enables Xauth for Cisco IPSec VPNs.
- `PasswordEncryption` (string): A string that either has the value `Prompt` or isn’t present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecauthentication_xauthobject)*