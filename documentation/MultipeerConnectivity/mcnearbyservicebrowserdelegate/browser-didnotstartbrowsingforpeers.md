# browser(_:didNotStartBrowsingForPeers:)

**Framework**: Multipeer Connectivity  
**Kind**: method

Called when a browser failed to start browsing for peers.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
optional func browser(_ browser: MCNearbyServiceBrowser, didNotStartBrowsingForPeers error: any Error)
```

## Parameters

- `browser`: The browser object that failed to start browsing.
- `error`: An error object indicating what went wrong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:didnotstartbrowsingforpeers:))*