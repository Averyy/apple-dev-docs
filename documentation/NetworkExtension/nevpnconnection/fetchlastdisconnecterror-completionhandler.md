# fetchLastDisconnectError(completionHandler:)

**Framework**: Network Extension  
**Kind**: method

Retrives the most recent error that caused the VPN to disconnect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func fetchLastDisconnectError() async throws
```

#### Discussion

If VPN system (including the IPsec client) generated the error, then the error uses the [`NEVPNConnectionErrorDomain`](nevpnconnectionerrordomain.md) error domain. If the error came from a tunnel provider app extension instead, then the error is the [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) that the provider passed when disconnecting the tunnel.

## Parameters

- `handler`: An error handler that receives the last disconnect error as a parameter.

## See Also

- [let NEVPNConnectionErrorDomain: String](nevpnconnectionerrordomain.md)
  The domain for errors resulting from VPN connection calls.
- [enum NEVPNConnectionError](nevpnconnectionerror.md)
  Error codes specific to VPN connections.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nevpnconnection/fetchlastdisconnecterror(completionhandler:))*