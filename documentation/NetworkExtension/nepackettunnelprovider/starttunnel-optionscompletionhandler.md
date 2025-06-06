# startTunnel(options:completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Start the network tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func startTunnel(options: [String : NSObject]? = nil) async throws
```

#### Discussion

This method is called by the system to start the network tunnel.

`NEPacketTunnelProvider` subclasses must override this method.

When the Packet Tunnel Provider executes the completionHandler block with a nil error parameter, it signals to the system that it is ready to begin handling network data. Therefore, the Packet Tunnel Provider should call [`setTunnelNetworkSettings(_:completionHandler:)`](netunnelprovider/settunnelnetworksettings(_:completionhandler:).md) and wait for it to complete before executing the completionHandler block.

The domain and code of the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object passed to the `completionHandler` block are defined by the Packet Tunnel Provider.

## Parameters

- `options`: A dictionary passed by the app that requested that the tunnel be started. If the starting app did not specify a dictionary of options then this parameter will be nil. If the tunnel was started via Connect On Demand, then this parameter will be nil.
- `completionHandler`: A block that must be executed when the tunnel is fully established, or when the tunnel cannot be started due to an error. If the tunnel was successfully established, then the error parameter must be set to nil. If an error occurred, the error parameter passed to this block must be set to a non-nil   object.

## See Also

- [func stopTunnel(with: NEProviderStopReason, completionHandler: () -> Void)](nepackettunnelprovider/stoptunnel(with:completionhandler:).md)
  Stop the network tunnel.
- [func cancelTunnelWithError((any Error)?)](nepackettunnelprovider/canceltunnelwitherror(_:).md)
  Stop the network tunnel from the Packet Tunnel Provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/starttunnel(options:completionhandler:))*