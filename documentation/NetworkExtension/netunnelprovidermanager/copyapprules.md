# copyAppRules()

**Framework**: Network Extension  
**Kind**: method

Returns a copy of the app rules currently set in the configuration.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func copyAppRules() -> [NEAppRule]?
```

## Mentions

- [Routing your VPN network traffic](routing-your-vpn-network-traffic.md)

#### Return Value

An array of [`NEAppRule`](neapprule.md) objects, or `nil` if the configuration doesn’t have any app rules.

#### Discussion

This method provides read-only access to the configuration’s app rules.

## See Also

- [class func loadAllFromPreferences(completionHandler: ([NETunnelProviderManager]?, (any Error)?) -> Void)](netunnelprovidermanager/loadallfrompreferences(completionhandler:).md)
  Read all of the VPN configurations created by the calling app that have previously been saved to the Network Extension preferences.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidermanager/copyapprules())*