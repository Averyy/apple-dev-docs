# localEndpoint

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

An object containing details about the socket’s local endpoint.

**Availability**:
- iOS 9.0+ - Deprecated in 18.0
- iPadOS 9.0+ - Deprecated in 18.0
- Mac Catalyst 13.1+ - Deprecated in 18.0
- macOS 10.15+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 2.0

## Declaration

```swift
var localEndpoint: NWEndpoint? { get }
```

```objc
@property (readonly, nullable) NWEndpoint * localEndpoint;
```

#### Discussion

This endpoint object may be `nil` when the system calls your [`handleNewFlow(_:)`](../nefilterdataprovider/handlenewflow%28_%29.md) method; if so, receiving network data populates the object. In such a case, the filter may still perform filtering, based on its socket type, socket family, or socket protocol.

## See Also

### Getting socket flow properties
- [var remoteEndpoint: NWEndpoint?](./remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [var remoteHostname: String?](./remotehostname.md)
  The flow’s remote hostname, if applicable.
- [class NEFilterFlow](../nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var socketFamily: Int32](./socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](./sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](./socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/localendpoint)*