# NWUDPSession

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

An object to manage a UDP session to a network endpoint.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.11+ - Deprecated in 15.0
- tvOS 17.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0

> **Deprecated**: Use the [`nw_connection_t`](../Network/nw_connection_t.md) type from the [Network](../Network/Network.md) framework instead.

## Declaration

```swift
class NWUDPSession
```

```objc
@interface NWUDPSession : NSObject
```

## Overview

Since UDP does not include a handshake with the remote endpoint as part of its protocol, it is up to the client of the UDP session to provide feedback on the viability of the current endpoint. If a session is opened to a hostname, the system will resolve that hostname into potentially several IP addresses. Once the session state is `NWUDPSessionStateReady`, the client should try to write and read datagrams. If there is no response from the remote endpoint, the client can try the next address that was resolved using `tryNextResolvedEndpoint`.

## Topics

### Monitoring the session state
- [var state: NWUDPSessionState](./nwudpsession/state.md)
  The current state of the UDP session.
- [enum NWUDPSessionState](./nwudpsessionstate.md)
- [var isViable: Bool](./nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.
### Selecting remote endpoints
- [var resolvedEndpoint: NWEndpoint?](./nwudpsession/resolvedendpoint.md)
  The currently targeted remote endpoint.
- [func tryNextResolvedEndpoint()](./nwudpsession/trynextresolvedendpoint%28%29.md)
  Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.
### Transferring data
- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](./nwudpsession/setreadhandler%28_,maxdatagrams%29.md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](./nwudpsession/writedatagram%28_,completionhandler%29.md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](./nwudpsession/writemultipledatagrams%28_,completionhandler%29.md)
  Write multiple datagrams.
- [var maximumDatagramLength: Int](./nwudpsession/maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.
### Canceling the session
- [func cancel()](./nwudpsession/cancel%28%29.md)
  Cancel the session.
### Responding to network changes
- [var hasBetterPath: Bool](./nwudpsession/hasbetterpath.md)
  If a session has a better path, new session would use a different interface.
- [init(upgradeFor: NWUDPSession)](./nwudpsession/init%28upgradefor%29.md)
  This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.
### Getting session properties
- [var endpoint: NWEndpoint](./nwudpsession/endpoint.md)
  The destination endpoint with which this session was created.
- [var currentPath: NWPath?](./nwudpsession/currentpath.md)
  The current evaluated path for the session’s [`resolvedEndpoint`](./nwudpsession/resolvedendpoint.md) property.
### Initializers
- [init(upgradeForSession: NWUDPSession)](./nwudpsession/init%28upgradeforsession%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession)*