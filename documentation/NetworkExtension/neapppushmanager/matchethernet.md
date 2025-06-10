# matchEthernet

**Framework**: Network Extension  
**Kind**: property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
var matchEthernet: Bool { get set }
```

#### Discussion

If set to YES NEAppPushProvider is started when iOS device is connected to an Ethernet network and the ethernet network is the primary route on the device. NEAppPushProvider must determine viability of its functionality on the network. If the network does not support its operation it must call [NEAppPushProvider unmatchEthernet:] method to stop itself.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/matchethernet)*