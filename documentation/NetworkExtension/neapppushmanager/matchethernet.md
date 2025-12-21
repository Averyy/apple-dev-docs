# matchEthernet

**Framework**: Network Extension  
**Kind**: property

A property that indicates Ethernet support for Local Push Connectivity.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var matchEthernet: Bool { get set }
```

#### Discussion

If this value is `true` (Swift) or `YES` (Objective-C), the system starts the [`NEAppPushProvider`](neapppushprovider.md) when the following criteria are true:

- The iOS device is connected to an Ethernet network.
- The Ethernet network is the primary route on the device.

Have your [`NEAppPushProvider`](neapppushprovider.md) determine that its functionality is viable on the network. If the network doesn’t support the provider running over Ethernet, your provider needs to call [`unmatchEthernet()`](neapppushprovider/unmatchethernet().md) to stop itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/matchethernet)*