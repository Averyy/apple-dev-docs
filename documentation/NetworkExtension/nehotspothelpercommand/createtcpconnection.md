# createTCPConnection(_:)

**Framework**: Network Extension  
**Kind**: method

Create a new TCP connection over the network associated with the command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func createTCPConnection(_ endpoint: NWEndpoint) -> NWTCPConnection
```

#### Return Value

A TCP connection that will connect over the network associated with the command.

#### Discussion

The TCP connection is started automatically. Use KVO to observe the connection’s `state` property to be notified when the connection is established or fails.

## Parameters

- `endpoint`: The remote host and port of the connection.

## See Also

- [func bind(to command: NEHotspotHelperCommand)](../Foundation/NSMutableURLRequest/bind(to:).md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
- [func createUDPSession(NWEndpoint) -> NWUDPSession](nehotspothelpercommand/createudpsession(_:).md)
  Creates a new UDP session over the network associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/createtcpconnection(_:))*