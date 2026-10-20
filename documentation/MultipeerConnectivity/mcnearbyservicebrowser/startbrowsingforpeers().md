# startBrowsingForPeers()

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Starts browsing for peers.

**Availability**:
- iOS 7.0+ - Deprecated in 27.0
- iPadOS 7.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.10+ - Deprecated in 27.0
- tvOS 10.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0

> **Deprecated**: Use Network Framework instead

## Declaration

```swift
func startBrowsingForPeers()
```

```objc
- (void) startBrowsingForPeers;
```

#### Discussion

After this method is called (until you call [`stopBrowsingForPeers()`](./stopbrowsingforpeers%28%29.md)), the framework calls your delegate’s [`browser(_:foundPeer:withDiscoveryInfo:)`](../mcnearbyservicebrowserdelegate/browser%28_,foundpeer,withdiscoveryinfo%29.md) and [`browser(_:lostPeer:)`](../mcnearbyservicebrowserdelegate/browser%28_,lostpeer%29.md) methods as new peers are found and lost.

## See Also

### Browsing for Peers
- [func stopBrowsingForPeers()](./stopbrowsingforpeers%28%29.md)
  Stops browsing for peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/startbrowsingforpeers())*