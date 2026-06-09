# NetworkVPNIPSec

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a VPN using the IPSec sub-type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIPSec
```

#### Discussion

Specify `com.apple.configuration.network.vpn.ipsec` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, macOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, macOS, Shared iPad, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**Shared secret**:

This configuration sets up an IPSec VPN using a shared secret and group name for authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.ipsec",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Corporate IPSec VPN",
        "HostName": "vpn.example.com",
        "Authentication": {
            "Method": "SharedSecret",
            "LocalIdentifier": "vpngroup",
            "LocalIdentifierType": "KeyID",
            "CredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100"
        }
    }
}
```

**Certificate**:

This configuration sets up an IPSec VPN using a certificate identity asset for authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.ipsec",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "VisibleName": "Corporate IPSec VPN (Certificate)",
        "HostName": "vpn.example.com",
        "Authentication": {
            "Method": "Certificate",
            "IdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4"
        }
    }
}
```

## Topics

### Objects
- [object NetworkVPNIPSecAuthenticationObject](networkvpnipsecauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIPSecDNSObject](networkvpnipsecdnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNIPSecIdleObject](networkvpnipsecidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIPSecOnDemandObject](networkvpnipsecondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIPSecProxiesObject](networkvpnipsecproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.

## Properties

- `Authentication` (NetworkVPNIPSecAuthenticationObject) *(required)*: Settings that control authentication.
- `DNS` (NetworkVPNIPSecDNSObject): A dictionary to use for all VPN types.
- `HostName` (string) *(required)*: The IP address or hostname of the VPN server.
- `Idle` (NetworkVPNIPSecIdleObject): Specifies details about how the system handles idle VPN connections.
- `OnDemand` (NetworkVPNIPSecOnDemandObject): Specifies details about how the system controls on-demand VPN.
- `OverridePrimary` (boolean): If `true`, the system sends all network traffic over VPN.
- `Proxies` (NetworkVPNIPSecProxiesObject): The dictionary to use to configure `Proxies` for use with `VPN`.
- `VisibleName` (string) *(required)*: The name of the VPN connection that the system displays on the device.

## See Also

- [object AccountCalDAV](accountcaldav.md)
  The declaration to configure a Calendar account.
- [object AccountCardDAV](accountcarddav.md)
  The declaration to configure a Contacts account.
- [object AccountExchange](accountexchange.md)
  The declaration to configure an Exchange account.
- [object AccountGoogle](accountgoogle.md)
  The declaration to configure a Google account.
- [object AccountLDAP](accountldap.md)
  The declaration to configure a Lightweight Directory Access Protocol (LDAP) account.
- [object AccountMail](accountmail.md)
  The declaration to configure a Mail account.
- [object AccountSubscribedCalendar](accountsubscribedcalendar.md)
  The declaration to configure a subscribed calendar.
- [object AppManaged](appmanaged.md)
  The declaration to configure a managed app.
- [object AppSettings](appsettings.md)
  The declaration to configure app settings.
- [object AudioAccessorySettings](audioaccessorysettings.md)
  The declaration to configure audio accessory settings.
- [object ContentCaching](contentcaching.md)
  The declaration to configure the Content Caching service.
- [object DiskManagementSettings](diskmanagementsettings.md)
  The declaration to configure disk management settings on the device.
- [object ExtensibleSSO](extensiblesso.md)
  The declaration to configure Extensible Single Sign-On.
- [object ExternalIntelligenceSettings](externalintelligencesettings.md)
  The declaration to configure External Intelligence Integrations settings.
- [object IntelligenceSettings](intelligencesettings.md)
  The declaration to configure Apple Intelligence settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnipsec)*