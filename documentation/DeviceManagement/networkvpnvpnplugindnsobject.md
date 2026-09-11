# NetworkVPNVPNPluginDNSObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary to use for all VPN types.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
object NetworkVPNVPNPluginDNSObject
```

## Properties

- `DomainName` (string): The primary domain of the tunnel.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that the system uses to authenticate the user to the DNS resolver.
- `SearchDomains` ([string]): The list of domain strings used to fully qualify single-label host names.
- `ServerAddresses` ([string]) *(required)*: The array of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.
- `SupplementalMatchDomains` ([string]): The list of domain strings used to determine which DNS queries use the DNS resolver settings in `ServerAddresses`. The system uses this key to create a split DNS configuration where it resolves only hosts in certain domains using the tunnel’s DNS resolver. The system uses the default resolver for hosts that aren’t in one of the domains in this list. If `SupplementalMatchDomains` contains the empty string it becomes the default domain. Split-tunnel configurations can direct all DNS queries to the VPN DNS servers before the primary DNS servers. If the VPN tunnel becomes the network’s default route, the servers listed in `ServerAddresses` become the default resolver and the system ignores the `SupplementalMatchDomains` list.
- `SupplementalMatchDomainsNoSearch` (boolean): If `true`, don’t append the domains in the `SupplementalMatchDomains` list to the resolver’s list of search domains.

## See Also

- [object NetworkVPNVPNPluginAuthenticationObject](networkvpnvpnpluginauthenticationobject.md)
  Settings that control authentication.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnvpnplugindnsobject)*