# stopTunnel(with:completionHandler:)

**Framework**: Network Extension  
**Kind**: method  
**Role**: Instance Method

Stop the network tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func stopTunnel(with reason: NEProviderStopReason, completionHandler: @escaping @Sendable () -> Void)
```

```swift
func stopTunnel(with reason: NEProviderStopReason) async
```

```objc
- (void) stopTunnelWithReason:(NEProviderStopReason) reason completionHandler:(void (^)()) completionHandler;
```

## Discussion

This method is called by the system to stop the network tunnel.

NEPacketTunnelProvider subclasses must override this method.

Do not use this method to stop the tunnel from the Packet Tunnel Provider. Use `cancelTunnelWithError`: instead.

## Parameters

- `reason`: An `NEProviderStopReason` code indicating why the tunnel is being stopped. Possible codes are listed in [`NEProvider`](../neprovider.md).
- `completionHandler`: A block that must be executed when the tunnel is fully stopped.

## See Also

### Managing the tunnel life cycle
- [func startTunnel(options: [String : NSObject]?, completionHandler: ((any Error)?) -> Void)](./starttunnel%28options,completionhandler%29.md)
  Start the network tunnel.
- [func cancelTunnelWithError((any Error)?)](./canceltunnelwitherror%28_%29.md)
  Stop the network tunnel from the Packet Tunnel Provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nepackettunnelprovider/stoptunnel(with:completionhandler:))*