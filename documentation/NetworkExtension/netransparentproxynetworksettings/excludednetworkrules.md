# excludedNetworkRules

**Framework**: Network Extension  
**Kind**: property

An array of rules that collectively specify what traffic to not route through the transparent proxy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var excludedNetworkRules: [NENetworkRule]? { get set }
```

#### Discussion

The following restrictions apply to each rule in the array:

- If the port string of the endpoint is `0` or is the empty string, then the address of the endpoint must be a non-wildcard address, such as `0.0.0.0` or `::`.
- If the address is a wildcard address (such as `0.0.0.0` or `::)`, then the port string of the endpoint must be non-empty and must not be `0`.
- A port string of `53` is not allowed. Use Destination Domain-based rules to match DNS traffic.
- The [`matchLocalNetwork`](nenetworkrule/matchlocalnetwork.md) property must be `nil`.
- The [`matchDirection`](nenetworkrule/matchdirection.md) property must be [`NETrafficDirection.outbound`](netrafficdirection/outbound.md).

## See Also

- [var includedNetworkRules: [NENetworkRule]?](netransparentproxynetworksettings/includednetworkrules.md)
  An array of rules that collectively specify what traffic to route through the transparent proxy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netransparentproxynetworksettings/excludednetworkrules)*