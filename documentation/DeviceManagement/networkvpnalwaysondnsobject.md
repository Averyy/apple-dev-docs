# NetworkVPNAlwaysOnDNSObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary to use for all VPN types.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNAlwaysOnDNSObject
```

## Properties

- `DomainName` (string): The primary domain of the tunnel.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that the system uses to authenticate the user to the DNS resolver.
- `Protocol` (string) *(required)*: The transport protocol to communicate with the DNS server.
- `SearchDomains` ([string]): The list of domain strings used to fully qualify single-label host names.
- `ServerAddresses` ([string]) *(required)*: The array of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.
- `ServerName` (string): The hostname of a DNS-over-TLS server to validate the server certificate, as defined in RFC 7858. If `ServerAddresses` isn’t specified, the system uses the hostname to determine the server addresses. This key is required if the `DNSProtocol` is `TLS`.
- `ServerURL` (string): The URI template of a DNS-over-HTTPS server, as defined in RFC 8484, which needs to use the `https://` scheme. The system uses the hostname or address in the URL to validate the server certificate. If `ServerAddresses` isn’t specified, the system uses the hostname or address in the URL to determine the server addresses. This key is required if the `DNSProtocol` is `HTTPS`.
- `SupplementalMatchDomains` ([string]): The list of domain strings used to determine which DNS queries use the DNS resolver settings in `ServerAddresses`. The system uses this key to create a split DNS configuration where it resolves only hosts in certain domains using the tunnel’s DNS resolver. The system uses the default resolver for hosts that aren’t in one of the domains in this list. If `SupplementalMatchDomains` contains the empty string it becomes the default domain. Split-tunnel configurations can direct all DNS queries to the VPN DNS servers before the primary DNS servers. If the VPN tunnel becomes the network’s default route, the servers listed in `ServerAddresses` become the default resolver and the system ignores the `SupplementalMatchDomains` list.
- `SupplementalMatchDomainsNoSearch` (boolean): If `true`, don’t append the domains in the `SupplementalMatchDomains` list to the resolver’s list of search domains.

## See Also

- [object NetworkVPNAlwaysOnAllowedCaptiveNetworkPluginElementObject](networkvpnalwaysonallowedcaptivenetworkpluginelementobject.md)
  The array of captive networking apps whose traffic is allowed outside the VPN tunnel, to perform captive network handling. Used only when `AllowAllCaptiveNetworkPlugins` is `false`.
- [object NetworkVPNAlwaysOnApplicationExceptionElementObject](networkvpnalwaysonapplicationexceptionelementobject.md)
  An array that contains an arbitrary number of apps whose connections occur outside the VPN.
- [object NetworkVPNAlwaysOnProxiesObject](networkvpnalwaysonproxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNAlwaysOnServiceExceptionElementObject](networkvpnalwaysonserviceexceptionelementobject.md)
  An array that contains an arbitrary number of service exceptions.
- [object NetworkVPNAlwaysOnTunnelConfigurationElementObject](networkvpnalwaysontunnelconfigurationelementobject.md)
  An array that contains an arbitrary number of tunnel configurations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnalwaysondnsobject)*