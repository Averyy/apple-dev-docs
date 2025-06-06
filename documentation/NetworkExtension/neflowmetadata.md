# NEFlowMetaData

**Framework**: Network Extension  
**Kind**: class

Additional information about data flowing through a per-app VPN provider.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
class NEFlowMetaData
```

#### Overview

This metadata is only present for data flowing through per-app VPN providers, that is, app proxy providers and packet tunnel providers in per-app VPN mode, as indicated by the [`routingMethod`](netunnelprovider/routingmethod.md) property.

## Topics

### Getting source app information
- [var sourceAppUniqueIdentifier: Data](neflowmetadata/sourceappuniqueidentifier.md)
  A data instance that contains a unique hash value for the source application.
- [var sourceAppSigningIdentifier: String](neflowmetadata/sourceappsigningidentifier.md)
  A string that contains the signing identifier of the source application.
- [var sourceAppAuditToken: Data?](neflowmetadata/sourceappaudittoken.md)
  The audit token of the source application of the flow.
### Getting flow information
- [var filterFlowIdentifier: UUID?](neflowmetadata/filterflowidentifier.md)
  The identifier of the content filter flow corresponding to this flow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NEPacket](nepacket.md)
  A network packet and its associated properties.
- [class NEAppProxyTCPFlow](neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [In-Provider Networking](in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
- [Handling Flow Copying](handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata)*