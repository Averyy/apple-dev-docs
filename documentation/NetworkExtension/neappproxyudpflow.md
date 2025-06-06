# NEAppProxyUDPFlow

**Framework**: Network Extension  
**Kind**: class

An object for reading and writing data to and from a UDP conversation being proxied by the provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppProxyUDPFlow
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

#### Overview

App Proxy Providers receive UDP connections to be proxied in the form of `NEAppProxyUDPFlow` objects.

## Topics

### Handling flow data
- [func readDatagrams(completionHandler: ([Data]?, [NWEndpoint]?, (any Error)?) -> Void)](neappproxyudpflow/readdatagrams(completionhandler:)-9z8gw.md)
  Read datagrams from the flow.
- [func writeDatagrams([Data], sentBy: [NWEndpoint], completionHandler: ((any Error)?) -> Void)](neappproxyudpflow/writedatagrams(_:sentby:completionhandler:).md)
  Write datagrams to the flow.
### Getting flow information
- [var localEndpoint: NWEndpoint?](neappproxyudpflow/localendpoint.md)
  An [`NWEndpoint`](nwendpoint.md) object containing information about the local endpoint of the flow.
### Instance Properties
- [var localFlowEndpoint: NWEndpoint?](neappproxyudpflow/localflowendpoint-7ukb6.md)
### Instance Methods
- [func readDatagrams() async -> ([(Data, NWEndpoint)]?, (any Error)?)](neappproxyudpflow/readdatagrams.md)
- [func readDatagrams(completionHandler: ([(Data, NWEndpoint)]?, (any Error)?) -> Void)](neappproxyudpflow/readdatagrams(completionhandler:)-71k28.md)
- [func writeDatagrams([(Data, NWEndpoint)]) async throws](neappproxyudpflow/writedatagrams(_:).md)
- [func writeDatagrams([(Data, NWEndpoint)], completionHandler: ((any Error)?) -> Void)](neappproxyudpflow/writedatagrams(_:completionhandler:).md)

## Relationships

### Inherits From
- [NEAppProxyFlow](neappproxyflow.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NEAppProxyTCPFlow](neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [class NEFlowMetaData](neflowmetadata.md)
  Additional information about data flowing through a per-app VPN provider.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
- [Handling Flow Copying](handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxyudpflow)*