# NetworkVPNIKEV2RulesElement_ActionParameterObject

**Framework**: Device Management  
**Kind**: dictionary

A dictionary that provides rules similar to the OnDemandRules dictionary, but evaluated on each connection instead of when the network changes. These dictionaries are evaluated in order, and the behavior is determined by the first dictionary that matches.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
object NetworkVPNIKEV2RulesElement_ActionParameterObject
```

#### Discussion

The keys allowed in each dictionary are described below. Note: This array is used only for dictionaries in which EvaluateConnection is the Action value.

## Properties

- `DomainAction` (string) *(required)*: Defines the VPN behavior for the specified domains. Allowed values are: - ‘ConnectIfNeeded’: The specified domains should trigger a VPN connection attempt if domain name resolution fails, such as when the DNS server indicates that it can’t resolve the domain, responds with a redirection to a different server, or fails to respond (timeout).
- ‘NeverConnect’: The specified domains should never trigger a VPN connection attempt.
- `Domains` ([string]) *(required)*: The domains to apply this evaluation.
- `RequiredDNSServers` ([string]): An array of IP addresses of DNS servers to use for resolving the specified domains. These servers don’t need to be part of the device’s current network configuration. If these DNS servers aren’t reachable, the system establishes a VPN connection. These DNS servers need to be either internal DNS servers or trusted external DNS servers. This key is valid only if the value of ‘DomainAction’ is ‘ConnectIfNeeded’.
- `RequiredURLStringProbe` (string): An HTTP or HTTPS (preferred) URL to probe, using a GET request. If the URL’s hostname can’t be resolved, if the server is unreachable, or if the server doesn’t respond with a 200 HTTP status code, a VPN connection is established in response. This key is valid only if the value of ‘DomainAction’ is ‘ConnectIfNeeded’.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/networkvpnikev2ruleselement_actionparameterobject)*