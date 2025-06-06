# probeURL

**Framework**: Network Extension  
**Kind**: property

An HTTP or HTTPS URL. If the rule matches the connection being established and the action is `NEEvaluateConnectionRuleActionConnectIfNeeded` and a request sent to this URL results in a response with an HTTP response code other than 200, then the VPN is started.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var probeURL: URL? { get set }
```

## See Also

- [var matchDomains: [String]](neevaluateconnectionrule/matchdomains.md)
  An array of domains used to match the destination hostname of connections. If the destination hostname of a connection matches any of the domains in the array, then the connection matches the rule. Each domain is matched against the destination hostname using suffix matching, and each label in the domain must match an entire label in the hostname. For example, the domain `example.com` will match the hostname `www.example.com` but not `www.anotherexample.com`.
- [var useDNSServers: [String]?](neevaluateconnectionrule/usednsservers.md)
  If the rule matches the connection being established and the action is `NEEvaluateConnectionRuleActionConnectIfNeeded`, the DNS servers specified in this array are used to resolve the destination hostname of the connection while evaluating connectivity to the destination of the connection. If the resolution fails for any reason, the VPN is started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neevaluateconnectionrule/probeurl)*