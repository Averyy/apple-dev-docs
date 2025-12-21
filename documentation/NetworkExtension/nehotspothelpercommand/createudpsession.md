# createUDPSession(_:)

**Framework**: Network Extension  
**Kind**: method

Creates a new UDP session over the network associated with the command.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func createUDPSession(_ endpoint: NWEndpoint) -> NWUDPSession
```

#### Return Value

A UDP session that will connect over the network associated with the command.

#### Discussion

The UDP session is started automatically. Use KVO to observe the session’s state property to be notified when the session is ready to send and receive UDP datagrams. For information about KVO see [`Key-Value Observing Programming Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/KeyValueObserving/KeyValueObserving.html#//apple_ref/doc/uid/10000177i).

## Parameters

- `endpoint`: The remote host and port of the session.

## See Also

- [func bind(to: NEHotspotHelperCommand)](../Foundation/NSMutableURLRequest/bind(to:).md)
  Binds a URL request to the network interface associated with the hotspot helper command instance.
- [func createTCPConnection(NWEndpoint) -> NWTCPConnection](nehotspothelpercommand/createtcpconnection(_:).md)
  Create a new TCP connection over the network associated with the command.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nehotspothelpercommand/createudpsession(_:))*