# browser(_:didNotStartBrowsingForPeers:)

**Framework**: Multipeer Connectivity  
**Kind**: method  
**Role**: Instance Method

Called when a browser failed to start browsing for peers.

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
optional func browser(_ browser: MCNearbyServiceBrowser, didNotStartBrowsingForPeers error: any Error)
```

```objc
- (void) browser:(MCNearbyServiceBrowser *) browser didNotStartBrowsingForPeers:(NSError *) error;
```

## Parameters

- `browser`: The browser object that failed to start browsing.
- `error`: An error object indicating what went wrong.


---

*[View on Apple Developer](https://developer.apple.com/documentation/multipeerconnectivity/mcnearbyservicebrowserdelegate/browser(_:didnotstartbrowsingforpeers:))*