# VPN.IPSec

**Framework**: Device Management  
**Kind**: dictionary

The dictionary to use for an IPSec VPN type.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- macOS 10.7+
- visionOS 1.0+

## Declaration

```swift
object VPN.IPSec
```

## Properties

- `AuthenticationMethod` (string): The authentication method for L2TP and Cisco IPSec.
- `DisconnectOnIdle` (integer): If `1`, disconnect after an on-demand connection idles.
- `DisconnectOnIdleTimer` (integer): The length of time to wait before disconnecting an on-demand connection.
- `LocalIdentifier` (string): The name of the group. For hybrid authentication, the string needs to end with “hybrid”. Present only for Cisco IPSec if `AuthenticationMethod` is `SharedSecret`.
- `LocalIdentifierType` (string): Present only if `AuthenticationMethod` is `SharedSecret`. The value is `KeyID`. The system uses this value for L2TP and Cisco IPSec VPNs.
- `OnDemandEnabled` (integer): If `1`, enables bringing the VPN connection up on demand.
- `OnDemandMatchDomainsAlways` ([string]): Deprecated. A list of domain names. In iOS 7 and later, if this key is present, the system treats associated domain names as though they’re associated with the `OnDemandMatchDomainsOnRetry` key. This behavior can be overridden by `OnDemandRules`. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandMatchDomainsNever` ([string]): Deprecated. A list of domain names. In iOS 7 and later, this key is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandMatchDomainsOnRetry` ([string]): Deprecated. A list of domain names. In iOS 7 and later, this field is deprecated (but still supported) in favor of `EvaluateConnection` actions in the `OnDemandRules` dictionaries. Deprecated: iOS 7+ | iPadOS 7+
- `OnDemandRules` ([VPN.VPN.OnDemandRulesElement]): The on-demand rules dictionary.
- `PayloadCertificateUUID` (string): The UUID of the certificate payload within the same profile to use for the account credentials. Only use this with Cisco IPSec VPNs and if the `AuthenticationMethod` key is to `Certificate`.
- `PromptForVPNPIN` (boolean): If `true`, prompts for a PIN when connecting to Cisco IPSec VPNs.
- `RemoteAddress` (string): The IP address or host name of the VPN server.
- `SharedSecret` (data): The shared secret for this VPN account. Only use this with L2TP and Cisco IPSec VPNs and if the `AuthenticationMethod` key is to `SharedSecret`.
- `XAuthEnabled` (integer): If `1`, enables Xauth for Cisco IPSec VPNs.
- `XAuthName` (string): The user name for the VPN account for Cisco IPSec.
- `XAuthPassword` (string): The VPN account password for Cisco IPSec.
- `XAuthPasswordEncryption` (string): A string that either has the value “Prompt” or isn’t present.

## See Also

- [object VPN.AlwaysOn](vpn/alwayson-data.dictionary.md)
  The dictionary that contains IPSec settings.
- [object VPN.DNS](vpn/dns-data.dictionary.md)
  The dictionary to configure DNS settings for the VPN.
- [object VPN.IKEv2](vpn/ikev2-data.dictionary.md)
  The dictionary to use for an IKEv2 VPN type.
- [object VPN.IPv4](vpn/ipv4-data.dictionary.md)
  The dictionary that contains IPV4 settings.
- [object VPN.PPP](vpn/ppp-data.dictionary.md)
  The dictionary that contains PPP settings.
- [object VPN.Proxies](vpn/proxies-data.dictionary.md)
  The dictionary that contains the Proxies settings.
- [object VPN.TransparentProxy](vpn/transparentproxy-data.dictionary.md)
  The dictionary to use for a transparent proxy VPN type.
- [object VPN.VPN](vpn/vpn-data.dictionary.md)
  The dictionary that contains VPN, IPSec, and IKEv2 settings.
- [object VPN.VendorConfig](vpn/vendorconfig-data.dictionary.md)
  The vendor-specific configuration dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/ipsec-data.dictionary)*