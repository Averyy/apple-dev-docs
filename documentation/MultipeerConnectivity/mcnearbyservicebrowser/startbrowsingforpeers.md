# startBrowsingForPeers()

**Framework**: Multipeer Connectivity  
**Kind**: method

Starts browsing for peers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func startBrowsingForPeers()
```

#### Discussion

After this method is called (until you call [`stopBrowsingForPeers()`](mcnearbyservicebrowser/stopbrowsingforpeers().md)), the framework calls your delegate’s [`browser(_:foundPeer:withDiscoveryInfo:)`](mcnearbyservicebrowserdelegate/browser(_:foundpeer:withdiscoveryinfo:).md) and [`browser(_:lostPeer:)`](mcnearbyservicebrowserdelegate/browser(_:lostpeer:).md) methods as new peers are found and lost.

## See Also

- [func stopBrowsingForPeers()](mcnearbyservicebrowser/stopbrowsingforpeers.md)
  Stops browsing for peers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowser/startbrowsingforpeers())*