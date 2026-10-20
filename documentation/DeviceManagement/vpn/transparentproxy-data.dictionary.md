# VPN.TransparentProxy

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Device Management Profile

The dictionary to use for a transparent proxy VPN type.

**Availability**:
- macOS 14.0+

## Declaration

```
object VPN.TransparentProxy
```

## Properties

- `AuthenticationMethod` (string): The type of authentication method to use: `Password`, `Certificate`, or `Password+Certificate`.

  **Default**: `Password`; **Allowed Values**: `Password`, `Certificate`, `Password+Certificate`
- `DisconnectOnIdle` (integer): If `1`, the VPN disconnects automatically disconnect after a period defined by `DisconnectOnIdleTimer`.

  **Default**: `0`; **Allowed Values**: `0`, `1`
- `DisconnectOnIdleTimer` (integer): The number of seconds before the VPN disconnects. This value is only used if `DisconnectOnIdle` is `1`.
- `EnforceRoutes` (integer): If `1`, then all the VPN’s non-default routes take precedence over any locally-defined routes. If `IncludeAllNetworks` is `1`, the system ignores the value of `EnforceRoutes`.

  **Default**: `0`; **Allowed Values**: `0`, `1`
- `OnDemandEnabled` (integer): If `1`, the system brings up the VPN on demand.

  **Default**: `0`; **Allowed Values**: `0`, `1`
- `OnDemandRules` ([VPN.VPN.OnDemandRulesElement]): Determines when and how the system uses an OnDemand VPN.
- `Order` (integer): A positive integer.
- `Password` (string): The password to use for the account credentials. Only used if `AuthenticationMethod` is `Password`.
- `PayloadCertificateUUID` (string): The UUID of the identity certificate as the account credential. If `AuthenticationMethod` is `Certificate`, and extended authentication (EAP) isn’t used, the device sends this certificate for IKE client authentication. If extended authentication is used, this certificate can be used for EAP-TLS.
- `ProviderBundleIdentifier` (string): If the VPNSubType field contains the bundle identifier of an app that contains multiple VPN providers of the same type (app-proxy or packet-tunnel), then the system uses this field to choose which provider to use for this configuration. If the VPN provider uses a system extension, then this field is required.
- `ProviderDesignatedRequirement` (string): If the VPN provider uses a system extension, then this field is required.
- `ProviderType` (string): If the value of this key is `app-proxy`, the VPN service tunnels traffic at the application layer. If the value of this key is `packet-tunnel`, the VPN service tunnels traffic at the IP layer.

  **Default**: `packet-tunnel`; **Allowed Values**: `packet-tunnel`, `app-proxy`

## See Also

### Objects
- [object VPN.AlwaysOn](./alwayson-data.dictionary.md)
  The dictionary that contains IPSec settings.
- [object VPN.DNS](./dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IKEv2](./ikev2-data.dictionary.md)
  The dictionary to use for an IKEv2 VPN type.
- [object VPN.IPSec](./ipsec-data.dictionary.md)
  The dictionary to use for an IPSec VPN type.
- [object VPN.IPv4](./ipv4-data.dictionary.md)
  The dictionary that contains IPV4 settings.
- [object VPN.PPP](./ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](./proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.VPN](./vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](./vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/transparentproxy-data.dictionary)*