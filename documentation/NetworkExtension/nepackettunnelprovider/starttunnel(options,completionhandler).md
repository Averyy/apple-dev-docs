# startTunnel(options:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

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
func startTunnel(options: [String : NSObject]? = nil, completionHandler: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func startTunnel(options: [String : NSObject]? = nil) async throws
```

```objc
- (void) startTunnelWithOptions:(NSDictionary<NSString *,NSObject *> *) options completionHandler:(void (^)(NSError *error)) completionHandler;
```

## Discussion

This method is called by the system to start the network tunnel.

`NEPacketTunnelProvider` subclasses must override this method.

When the Packet Tunnel Provider executes the completionHandler block with a nil error parameter, it signals to the system that it is ready to begin handling network data. Therefore, the Packet Tunnel Provider should call [`setTunnelNetworkSettings(_:completionHandler:)`](../netunnelprovider/settunnelnetworksettings%28_,completionhandler%29.md) and wait for it to complete before executing the completionHandler block.

The domain and code of the [`NSError`](../../Foundation/nserror.md) object passed to the `completionHandler` block are defined by the Packet Tunnel Provider.

## Parameters

- `options`: A dictionary passed by the app that requested that the tunnel be started. If the starting app did not specify a dictionary of options then this parameter will be nil. If the tunnel was started via Connect On Demand, then this parameter will be nil.
- `completionHandler`: A block that must be executed when the tunnel is fully established, or when the tunnel cannot be started due to an error. If the tunnel was successfully established, then the error parameter must be set to nil. If an error occurred, the error parameter passed to this block must be set to a non-nil [`NSError`](../../Foundation/nserror.md) object.

## See Also

### Managing the tunnel life cycle
- [func stopTunnel(with: NEProviderStopReason, completionHandler: () -> Void)](./stoptunnel%28with,completionhandler%29.md)
  Stop the network tunnel.
- [func cancelTunnelWithError((any Error)?)](./canceltunnelwitherror%28_%29.md)
  Stop the network tunnel from the Packet Tunnel Provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/starttunnel(options:completionhandler:))*