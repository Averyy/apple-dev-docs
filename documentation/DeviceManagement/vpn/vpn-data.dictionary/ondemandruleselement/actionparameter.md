# VPN.VPN.OnDemandRulesElement.ActionParameter

**Framework**: Device Management  
**Kind**: dictionary

Dictionary containing parameters for action settings

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- macOS 10.7+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
object VPN.VPN.OnDemandRulesElement.ActionParameter
```

## Properties

- `DomainAction` (string) *(required)*: Defines the VPN behavior for the specified domains. Allowed values are: - ‘ConnectIfNeeded’: The specified domains should trigger a VPN connection attempt if domain name resolution fails, such as when the DNS server indicates that it can’t resolve the domain, responds with a redirection to a different server, or fails to respond (timeout).
- ‘NeverConnect’: The specified domains should never trigger a VPN connection attempt.
- `Domains` ([string]) *(required)*: The domains to apply this evaluation.
- `RequiredDNSServers` ([string]): An array of IP addresses of DNS servers to use for resolving the specified domains. These servers don’t need to be part of the device’s current network configuration. If these DNS servers aren’t reachable, the system establishes a VPN connection. These DNS servers need to be either internal DNS servers or trusted external DNS servers. This key is valid only if the value of ‘DomainAction’ is ‘ConnectIfNeeded’.
- `RequiredURLStringProbe` (string): An HTTP or HTTPS (preferred) URL to probe, using a GET request. If the URL’s hostname can’t be resolved, if the server is unreachable, or if the server doesn’t respond with a 200 HTTP status code, a VPN connection is established in response. This key is valid only if the value of ‘DomainAction’ is ‘ConnectIfNeeded’.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/vpn/vpn-data.dictionary/ondemandruleselement/actionparameter)*