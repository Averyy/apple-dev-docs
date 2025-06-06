# matchPrivateLTENetworks

**Framework**: Network Extension  
**Kind**: property

An array of private LTE networks that the system matches for local push activation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
var matchPrivateLTENetworks: [NEPrivateLTENetwork] { get set }
```

#### Discussion

If the properties of current private LTE network matches with the properties of a member of this array then the system starts the [`NEAppPushProvider`](neapppushprovider.md). The array must contain at least one SSID to start the provider, and has an upper limit of 10 private LTE networks. For private LTE networks that aren’t band 48, only supervised devices can perform the match.

## See Also

- [var matchSSIDs: [String]](neapppushmanager/matchssids.md)
  An array of Wi-Fi SSID strings that the system matches for local push activation.
- [class NEPrivateLTENetwork](neprivateltenetwork.md)
  The parameters of a private LTE network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/matchprivateltenetworks)*