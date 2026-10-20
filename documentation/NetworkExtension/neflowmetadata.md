# NEFlowMetaData

**Framework**: Network Extension  
**Kind**: class  
**Role**: Class

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

```objc
@interface NEFlowMetaData : NSObject
```

#### Overview

This metadata is only present for data flowing through per-app VPN providers, that is, app proxy providers and packet tunnel providers in per-app VPN mode, as indicated by the [`routingMethod`](./netunnelprovider/routingmethod.md) property.

## Topics

### Getting source app information
- [var sourceAppUniqueIdentifier: Data](./neflowmetadata/sourceappuniqueidentifier.md)
  A data instance that contains a unique hash value for the source application.
- [var sourceAppSigningIdentifier: String](./neflowmetadata/sourceappsigningidentifier.md)
  A string that contains the signing identifier of the source application.
- [var sourceAppAuditToken: Data?](./neflowmetadata/sourceappaudittoken.md)
  The audit token of the source application of the flow.
### Getting flow information
- [var filterFlowIdentifier: UUID?](./neflowmetadata/filterflowidentifier.md)
  The identifier of the content filter flow corresponding to this flow.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Related Documentation
- [class NEPacket](./nepacket.md)
  A network packet and its associated properties.
### Flow handling
- [class NEAppProxyTCPFlow](./neappproxytcpflow.md)
  An object for reading and writing data to and from a TCP connection being proxied by the provider.
- [class NEAppProxyUDPFlow](./neappproxyudpflow.md)
  An object for reading and writing data to and from a UDP conversation being proxied by the provider.
- [class NEAppProxyFlow](./neappproxyflow.md)
  An abstract base class shared by NEAppProxyTCPFlow and NEAppProxyUDPFlow.
- [In-Provider Networking](./in-provider-networking.md)
  Network APIs for use by all types of NetworkExtension providers and by hotspot helpers.
- [Handling Flow Copying](./handling-flow-copying.md)
  Exchange data streams by using proxy-provider classes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/neflowmetadata)*