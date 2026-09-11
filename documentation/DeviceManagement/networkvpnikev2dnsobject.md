# NetworkVPNIKEV2DNSObject

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
object NetworkVPNIKEV2DNSObject
```

## Properties

- `DomainName` (string): The primary domain of the tunnel.
- `IdentityAssetReference` (string): The identifier of a credential asset declaration that contains the identity that the system uses to authenticate the user to the DNS resolver.
- `SearchDomains` ([string]): The list of domain strings used to fully qualify single-label host names.
- `ServerAddresses` ([string]) *(required)*: The array of DNS server IP address strings. These IP addresses can be a mixture of IPv4 and IPv6 addresses.
- `SupplementalMatchDomains` ([string]): The list of domain strings used to determine which DNS queries use the DNS resolver settings in `ServerAddresses`. The system uses this key to create a split DNS configuration where it resolves only hosts in certain domains using the tunnel’s DNS resolver. The system uses the default resolver for hosts that aren’t in one of the domains in this list. If `SupplementalMatchDomains` contains the empty string it becomes the default domain. Split-tunnel configurations can direct all DNS queries to the VPN DNS servers before the primary DNS servers. If the VPN tunnel becomes the network’s default route, the servers listed in `ServerAddresses` become the default resolver and the system ignores the `SupplementalMatchDomains` list.
- `SupplementalMatchDomainsNoSearch` (boolean): If `true`, don’t append the domains in the `SupplementalMatchDomains` list to the resolver’s list of search domains.

## See Also

- [object NetworkVPNIKEV2AuthenticationObject](networkvpnikev2authenticationobject.md)
  Settings that control authentication.
- [object NetworkVPNIKEV2IdleObject](networkvpnikev2idleobject.md)
  Specifies details about how the system handles idle VPN connections.
- [object NetworkVPNIKEV2NetworkRoutingObject](networkvpnikev2networkroutingobject.md)
  Specifies details about how the VPN routes different types of network traffic.
- [object NetworkVPNIKEV2OnDemandObject](networkvpnikev2ondemandobject.md)
  Specifies details about how the system controls on-demand VPN.
- [object NetworkVPNIKEV2PostQuantumKeyExchangeObject](networkvpnikev2postquantumkeyexchangeobject.md)
  Post Quantum Key Exchange settings.
- [object NetworkVPNIKEV2ProxiesObject](networkvpnikev2proxiesobject.md)
  The dictionary to use to configure `Proxies` for use with `VPN`.
- [object NetworkVPNIKEV2SecurityAssociationParametersObject](networkvpnikev2securityassociationparametersobject.md)
  These parameters apply to Child Security Association unless `ChildSecurityAssociationParameters` is specified.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2dnsobject)*