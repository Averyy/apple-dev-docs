# matchSSIDs

**Framework**: Network Extension  
**Kind**: property

An array of Wi-Fi SSID strings that the system matches for local push activation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var matchSSIDs: [String] { get set }
```

## Mentions

- [Maintaining a Reliable Network Connection](maintaining-a-reliable-network-connection.md)

#### Discussion

If the SSID string of the current Wi-Fi network matches a member of this array, the framework starts the [`NEAppPushProvider`](neapppushprovider.md). The array must contain at least one SSID to start the provider, and has an upper limit of 10 SSIDs.

## See Also

- [var matchPrivateLTENetworks: [NEPrivateLTENetwork]](neapppushmanager/matchprivateltenetworks.md)
  An array of private LTE networks that the system matches for local push activation.
- [class NEPrivateLTENetwork](neprivateltenetwork.md)
  The parameters of a private LTE network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neapppushmanager/matchssids)*