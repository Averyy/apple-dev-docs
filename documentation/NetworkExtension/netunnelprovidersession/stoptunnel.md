# stopTunnel()

**Framework**: Network Extension  
**Kind**: method

Start the process of disconnecting the tunnel.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func stopTunnel()
```

#### Discussion

This method returns immediately after starting the process of disconnecting the tunnel. In order to be notified when the tunnel is fully disconnected, register to observe the [`NEVPNStatusDidChangeNotification`](nevpnstatusdidchangenotification.md) notification on the [`NETunnelProviderSession`](netunnelprovidersession.md) object and examine its status property when the notification is received.

## See Also

- [func startTunnel(options: [String : Any]?) throws](netunnelprovidersession/starttunnel(options:).md)
  Start the process of connecting the tunnel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/netunnelprovidersession/stoptunnel())*