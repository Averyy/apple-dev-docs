# cancelTunnelWithError(_:)

**Framework**: Network Extension  
**Kind**: method

Stop the network tunnel from the Packet Tunnel Provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func cancelTunnelWithError(_ error: (any Error)?)
```

#### Discussion

The Packet Tunnel Provider should call this method when an unrecoverable error occurs, such as the tunnel server going down or the VPN authentication session expiring.

## Parameters

- `error`: An   object containing the error that caused the tunnel to be stopped. The domain and code of this NSError object is defined by the caller.

## See Also

- [func startTunnel(options: [String : NSObject]?, completionHandler: ((any Error)?) -> Void)](nepackettunnelprovider/starttunnel(options:completionhandler:).md)
  Start the network tunnel.
- [func stopTunnel(with: NEProviderStopReason, completionHandler: () -> Void)](nepackettunnelprovider/stoptunnel(with:completionhandler:).md)
  Stop the network tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/canceltunnelwitherror(_:))*