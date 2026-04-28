# DNSSettings.OnDemandRulesElement

**Framework**: Device Management  
**Kind**: dictionary

A list of domain strings that determine which DNS queries use the DNS server.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object DNSSettings.OnDemandRulesElement
```

## Topics

### Objects
- [object DNSSettings.OnDemandRulesElement.ActionParameter](dnssettings/ondemandruleselement/actionparameter.md)
  A dictionary that provides per-connection rules.

## Properties

- `Action` (string) *(required)*: The action to take if this dictionary matches the current network. Allowed values: - `Connect`: Apply DNS Settings when the dictionary matches.
- `Disconnect`: Don’t apply DNS Settings when the dictionary matches.
- `EvaluateConnection`: Apply DNS Settings with per-domain exceptions when the dictionary matches.
- `ActionParameters` ([DNSSettings.OnDemandRulesElement.ActionParameter]): An array of dictionaries that provide per-connection rules. The system uses this array only for settings where the `Action` value is `EvaluateConnection`.
- `DNSDomainMatch` ([string]): An array of domain names. This rule matches if any of the domain names in the specified list matches any domain in the device’s search domains list. The system supports a single wildcard (`*`) prefix, but it’s not required. For example, both `*.example.com` and `example.com` match against `mydomain.example.com` and `your.domain.example.com`, but don’t match against `mydomain-example.com`.
- `DNSServerAddressMatch` ([string]): An array of IP addresses. This rule matches if any of the network’s specified DNS servers match any entry in the array. The system supports matching with a single wildcard. For example, `17.*` matches any DNS server in the 17.0.0.0/8 subnet.
- `InterfaceTypeMatch` (string): An interface type. If specified, this rule matches only if the primary network interface hardware matches the specified type.
- `SSIDMatch` ([string]): An array of SSIDs to match against the current network. If the network isn’t a Wi-Fi network or if the SSID doesn’t appear in this array, the match fails. Omit this key and the corresponding array to match against any SSID.
- `URLStringProbe` (string): A URL to probe. This rule matches if this URL is successfully fetched and returns a 200 HTTP status code without redirection.

## See Also

- [object DNSSettings.DNSSettings](dnssettings/dnssettings-data.dictionary.md)
  A dictionary that defines a configuration for an encrypted DNS server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/dnssettings/ondemandruleselement)*