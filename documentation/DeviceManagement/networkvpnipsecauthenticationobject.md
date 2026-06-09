# NetworkVPNIPSecAuthenticationObject

**Framework**: Device Management  
**Kind**: dictionary

Settings that control authentication.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSecAuthenticationObject
```

## Topics

### Objects
- [object NetworkVPNIPSecAuthentication_XAuthObject](networkvpnipsecauthentication_xauthobject.md)
  Settings that control XAuth.

## Properties

- `CredentialsAssetReference` (string): The identifier of an asset declaration that contains the credentials (password) to authenticate with the VPN servers. Only use this with Cisco IPSec VPNs and if the `Authentication.Method` key is to `SharedSecret`.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that this account requires to authenticate with the VPN servers. Only use this with Cisco IPSec VPNs and if the `Authentication.Method` key is to `Certificate`.
- `LocalIdentifier` (string): The name of the group. For hybrid authentication, the string needs to end with “hybrid”. Present only for Cisco IPSec if `Authentication.Method` is `SharedSecret`.
- `LocalIdentifierType` (string): Present only if `Authentication.Method` is `SharedSecret`. The value is `KeyID`. The system uses this value for Cisco IPSec VPNs.
- `Method` (string) *(required)*: The authentication method to use.
- `PromptForVPNPIN` (boolean): If `true`, prompts for a PIN when connecting to Cisco IPSec VPNs.
- `XAuth` (NetworkVPNIPSecAuthentication_XAuthObject): Settings that control XAuth.

## See Also

- [object NetworkVPNIPSecDNSObject](networkvpnipsecdnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIPSecIdleObject](networkvpnipsecidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIPSecOnDemandObject](networkvpnipsecondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIPSecProxiesObject](networkvpnipsecproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsecauthenticationobject)*