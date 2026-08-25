# NetworkVPNVPNPlugin

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a VPN using the VPN plugin sub-type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNVPNPlugin
```

#### Discussion

Specify `com.apple.configuration.network.vpn.vpn-plugin` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, tvOS, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in system scope | iOS, macOS, Shared iPad, tvOS, visionOS |
| Allowed in user scope | N/A |
| Apply | Multiple configurations are applied separately |

##### Configuration Examples

**Password**:

This configuration sets up a VPN plugin using username and password credentials from an asset.

```json
{
    "Type": "com.apple.configuration.network.vpn.vpn-plugin",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Corporate VPN",
        "HostName": "vpn.example.com",
        "SubType": "com.example.vpn.plugin",
        "Authentication": {
            "Method": "Password",
            "CredentialsAssetReference": "64BF8F5C-8CFD-40AA-9082-A0B594D4E100"
        }
    }
}
```

**Certificate**:

This configuration sets up a VPN plugin using a certificate identity asset for authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.vpn-plugin",
    "Identifier": "2A3B4C5D-6E7F-8A9B-0C1D-2E3F4A5B6C7D",
    "ServerToken": "F1E2D3C4-B5A6-7890-ABCD-EF1234567890",
    "Payload": {
        "VisibleName": "Corporate VPN (Certificate)",
        "HostName": "vpn.example.com",
        "SubType": "com.example.vpn.plugin",
        "Authentication": {
            "Method": "Certificate",
            "IdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4"
        }
    }
}
```

## Topics

### Objects
- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNVPNPluginDNSObject](networkvpnvpnplugindnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNVPNPluginIdleObject](networkvpnvpnpluginidleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNVPNPluginNetworkRoutingObject](networkvpnvpnpluginnetworkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNVPNPluginOnDemandObject](networkvpnvpnpluginondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNVPNPluginProviderObject](networkvpnvpnpluginproviderobject.md)
  Specifies details about the provider.
- [object NetworkVPNVPNPluginProxiesObject](networkvpnvpnpluginproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNVPNPluginVendorConfigObject](networkvpnvpnpluginvendorconfigobject.md)
  The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.

## Properties

- `Authentication` (NetworkVPNVPNPluginAuthenticationObject) *(required)*: Settings that control authentication.
- `DNS` (NetworkVPNVPNPluginDNSObject): A dictionary to use for all VPN types.
- `HostName` (string) *(required)*: The IP address or hostname of the VPN server.
- `Idle` (NetworkVPNVPNPluginIdleObject): Specifies details about how the system handles idle VPN connections.
- `NetworkRouting` (NetworkVPNVPNPluginNetworkRoutingObject): Specifies details about how the VPN routes different types of network traffic. Available: iOS 27+ | iPadOS 27+ | macOS 27+ | visionOS 27+
- `OnDemand` (NetworkVPNVPNPluginOnDemandObject): Specifies details about how the system controls on-demand VPN.
- `Provider` (NetworkVPNVPNPluginProviderObject): Specifies details about the provider.
- `Proxies` (NetworkVPNVPNPluginProxiesObject): The dictionary to use to configure `Proxies` for use with `VPN`.
- `SubType` (string) *(required)*: An identifier for a vendor-specified configuration dictionary. If the configuration targets a VPN solution that uses a VPN plugin, then this field contains the bundle identifier of the plugin. Here are some examples: - Cisco AnyConnect: `com.cisco.anyconnect.applevpn.plugin`
- Juniper SSL: `net.juniper.sslvpn`
- F5 SSL: `com.f5.F5-Edge-Client.vpnplugin`
- SonicWALL Mobile Connect: `com.sonicwall.SonicWALL-SSLVPN.vpnplugin`
- ``Aruba VIA: `com.arubanetworks.aruba-via.vpnplugin` If the configuration targets a VPN solution that uses a network extension provider, then this field contains the bundle identifier of the app that contains the provider. Contact the VPN solution vendor for the value of the identifier.
- `VendorConfig` (NetworkVPNVPNPluginVendorConfigObject): The vendor-specific configuration dictionary, which the system reads only when `SubType` has a value.
- `VisibleName` (string) *(required)*: The name of the VPN connection that the system displays on the device.

## See Also

- [object AccessibilitySettings](accessibilitysettings.md)
  The declaration to configure accessibility settings.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnplugin)*