# NEAppProxyTCPFlow

**Framework**: Network Extension  
**Kind**: class

An object for reading and writing data to and from a TCP connection being proxied by the provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEAppProxyTCPFlow
```

## Mentions

- [Handling Flow Copying](handling-flow-copying.md)

#### Overview

App Proxy Providers receive TCP connections to be proxied in the form of `NEAppProxyTCPFlow` objects.

## Topics

### Handling flow data
- [func write(Data, withCompletionHandler: ((any Error)?) -> Void)](neappproxytcpflow/write(_:withcompletionhandler:).md)
  Write data to the flow.
- [func readData(completionHandler: (Data?, (any Error)?) -> Void)](neappproxytcpflow/readdata(completionhandler:).md)
  Read data from the flow.
### Getting flow information
- [var remoteEndpoint: NWEndpoint](neappproxytcpflow/remoteendpoint.md)
  An [`NWEndpoint`](nwendpoint.md) object containing information about the intended remote endpoint of the flow.
### Instance Properties
- [var remoteFlowEndpoint: NWEndpoint](neappproxytcpflow/remoteflowendpoint-4r7v1.md)

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

- [class NEAppProxyUDPFlow](neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [class NEFlowMetaData](neflowmetadata.md)
  Additional information about data flowing through a per-app VPN provider.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
- [Handling Flow Copying](handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neappproxytcpflow)*