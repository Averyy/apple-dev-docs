# NWUDPSession

**Framework**: Network Extension  
**Kind**: class

An object to manage a UDP session to a network endpoint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
class NWUDPSession
```

#### Overview

Since UDP does not include a handshake with the remote endpoint as part of its protocol, it is up to the client of the UDP session to provide feedback on the viability of the current endpoint. If a session is opened to a hostname, the system will resolve that hostname into potentially several IP addresses. Once the session state is `NWUDPSessionStateReady`, the client should try to write and read datagrams. If there is no response from the remote endpoint, the client can try the next address that was resolved using `tryNextResolvedEndpoint`.

## Topics

### Monitoring the session state
- [var state: NWUDPSessionState](nwudpsession/state.md)
  The current state of the UDP session.
- [enum NWUDPSessionState](nwudpsessionstate.md)
- [var isViable: Bool](nwudpsession/isviable.md)
  The viability of a UDP session represents whether or not data can be transferred.
### Selecting remote endpoints
- [var resolvedEndpoint: NWEndpoint?](nwudpsession/resolvedendpoint.md)
  The currently targeted remote endpoint.
- [func tryNextResolvedEndpoint()](nwudpsession/trynextresolvedendpoint.md)
  Mark the current value of resolvedEndpoint as unusable, and try to switch to the next available endpoint.
### Transferring data
- [func setReadHandler(([Data]?, (any Error)?) -> Void, maxDatagrams: Int)](nwudpsession/setreadhandler(_:maxdatagrams:).md)
  Set a read handler for datagrams.
- [func writeDatagram(Data, completionHandler: ((any Error)?) -> Void)](nwudpsession/writedatagram(_:completionhandler:).md)
  Write a single datagram.
- [func writeMultipleDatagrams([Data], completionHandler: ((any Error)?) -> Void)](nwudpsession/writemultipledatagrams(_:completionhandler:).md)
  Write multiple datagrams.
- [var maximumDatagramLength: Int](nwudpsession/maximumdatagramlength.md)
  The maximum size of a datagram to be written currently.
### Canceling the session
- [func cancel()](nwudpsession/cancel.md)
  Cancel the session.
### Responding to network changes
- [var hasBetterPath: Bool](nwudpsession/hasbetterpath.md)
  If a session has a better path, new session would use a different interface.
- [init(upgradeFor: NWUDPSession)](nwudpsession/init(upgradefor:).md)
  This convenience initializer can be used to create a new session based on the original session’s endpoint and parameters.
### Getting session properties
- [var endpoint: NWEndpoint](nwudpsession/endpoint.md)
  The destination endpoint with which this session was created.
- [var currentPath: NWPath?](nwudpsession/currentpath.md)
  The current evaluated path for the session’s [`resolvedEndpoint`](nwudpsession/resolvedendpoint.md) property.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nwudpsession)*