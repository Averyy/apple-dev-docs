# VPN.VPN.OnDemandRulesElement

**Framework**: Device Management  
**Kind**: dictionary

An On Demand rule

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
object VPN.VPN.OnDemandRulesElement
```

## Topics

### Objects
- [object VPN.VPN.OnDemandRulesElement.ActionParameter](vpn/vpn-data.dictionary/ondemandruleselement/actionparameter.md)
  Dictionary containing parameters for action settings

## Properties

- `Action` (string) *(required)*: The action to take if this dictionary matches the current network. Possible values are: - `Allow`: Deprecated. Allow VPN On Demand to connect if triggered.
- `Connect`: Unconditionally initiate a VPN connection on the next network attempt.
- `Disconnect`: Tear down the VPN connection and don’t reconnect on demand as long as this dictionary matches.
- `EvaluateConnection`: Evaluate the ActionParameters array for each connection attempt.
- `Ignore`: Leave any existing VPN connection up, but don’t reconnect on demand as long as this dictionary matches. Only the `Disconnect` action is available on watchOS 10 and later.
- `ActionParameters` ([VPN.VPN.OnDemandRulesElement.ActionParameter]): An array of dictionaries that provides rules similar to the `OnDemandRules` dictionary, but evaluated on each connection instead of when the network changes. This value is only for use with dictionaries in which the `Action` value is `EvaluateConnection`. The system evaluates these dictionaries in order and the first dictionary that matches determines the behavior. Not available in watchOS.
- `DNSDomainMatch` ([string]): An array of domain names. This rule matches if any of the domain names in the specified list matches any domain in the device’s search domains list. The system supports a wildcard (`*`) prefix. For example, `*.example.com` matches against either `mydomain.example.com` or `yourdomain.example.com`.
- `DNSServerAddressMatch` ([string]): An array of IP addresses. This rule matches if any of the network’s specified DNS servers match any entry in the array. The system supports matching with a single wildcard. For example, `17.*` matches any DNS server in the `17.0.0.0/8` subnet.
- `InterfaceTypeMatch` (string): An interface type. If specified, this rule matches only if the primary network interface hardware matches the specified type.
- `SSIDMatch` ([string]): An array of SSIDs to match against the current network. If the network isn’t a Wi-Fi network or if the SSID doesn’t appear in this array, the match fails. Omit this key and the corresponding array to match against any SSID.
- `URLStringProbe` (string): A URL to probe. This rule matches when this URL is successfully fetched (returns a `200` HTTP status code) without redirection. Not available in watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/vpn-data.dictionary/ondemandruleselement)*