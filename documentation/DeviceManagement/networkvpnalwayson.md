# NetworkVPNAlwaysOn

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure a VPN using the Always On sub-type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOn
```

#### Discussion

Specify `com.apple.configuration.network.vpn.always-on` as the declaration type.

##### Configuration Availability

|  |  |
| --- | --- |
| Allowed in supervised enrollment | iOS, Shared iPad, visionOS |
| Allowed in device enrollment | iOS, Shared iPad, visionOS |
| Allowed in user enrollment | N/A |
| Allowed in local enrollment | iOS, Shared iPad, visionOS |
| Allowed in system scope | iOS, Shared iPad, visionOS |
| Allowed in user scope | N/A |
| Apply | Only a single configuration is applied |

##### Configuration Example

This configuration sets up an always-on IKEv2 VPN for both Cellular and Wi-Fi interfaces using certificate authentication.

```json
{
    "Type": "com.apple.configuration.network.vpn.always-on",
    "Identifier": "EB13EE2B-5D63-4EBA-810F-5B81D07F5017",
    "ServerToken": "E180CA9A-F089-4FA3-BBDF-94CC159C4AE8",
    "Payload": {
        "VisibleName": "Always-On VPN",
        "UIToggleEnabled": false,
        "TunnelConfigurations": [
            {
                "ProtocolType": "IKEv2",
                "Interfaces": [
                    "Cellular",
                    "WiFi"
                ],
                "IKEV2": {
                    "HostName": "vpn.example.com",
                    "LocalIdentifier": "device@example.com",
                    "RemoteIdentifier": "vpn.example.com",
                    "Authentication": {
                        "Method": "Certificate",
                        "IdentityAssetReference": "CB3E6C7F-2318-437B-8A9E-D50C69376DE4"
                    }
                }
            }
        ]
    }
}
```

## Topics

### Objects
- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnApplicationExceptionElementObject](networkvpnalwaysonapplicationexceptionelementobject.md)
  An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- [object NetworkVPNAlwaysOnDNSObject](networkvpnalwaysondnsobject.md)
  A dictionary to use for all VPN types.
- [object NetworkVPNAlwaysOnProxiesObject](networkvpnalwaysonproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNAlwaysOnServiceExceptionElementObject](networkvpnalwaysonserviceexceptionelementobject.md)
  An array that contains an arbitrary number of service exceptions.
- [object NetworkVPNAlwaysOnTunnelConfigurationElementObject](networkvpnalwaysontunnelconfigurationelementobject.md)
  An array that contains an arbitrary number of tunnel configurations.

## Properties

- `AllowAllCaptiveNetworkPlugins` (boolean): If `true`, allows traffic from all captive networking apps outside the VPN tunnel to perform captive network handling.
- `AllowCaptiveWebSheet` (boolean): If `true`, allows traffic from Captive Web Sheet outside the VPN tunnel.
- `AllowedCaptiveNetworkPlugins` ([NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject]): The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- `ApplicationExceptions` ([NetworkVPNAlwaysOnApplicationExceptionElementObject]): An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- `DNS` (NetworkVPNAlwaysOnDNSObject): A dictionary to use for all VPN types.
- `Proxies` (NetworkVPNAlwaysOnProxiesObject): The dictionary to use to configure `Proxies` for use with `VPN`.
- `ServiceExceptions` ([NetworkVPNAlwaysOnServiceExceptionElementObject]): An array that contains an arbitrary number of service exceptions.
- `TunnelConfigurations` ([NetworkVPNAlwaysOnTunnelConfigurationElementObject]) *(required)*: An array that contains an arbitrary number of tunnel configurations.
- `UIToggleEnabled` (boolean): If `true`, allows the user to disable the VPN configuration.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwayson)*