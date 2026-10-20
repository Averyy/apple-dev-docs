# remoteHostname

**Framework**: Network Extension  
**Kind**: property  
**Role**: Instance Property

The flow’s remote hostname, if applicable.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var remoteHostname: String? { get }
```

```objc
@property (readonly, nullable) NSString * remoteHostname;
```

#### Discussion

This property is only populated for flows originating from create-by-name APIs like [`URLSession`](../../Foundation/urlsession.md) or [Network](../../Network/Network.md).

## See Also

### Getting socket flow properties
- [var remoteEndpoint: NWEndpoint?](./remoteendpoint.md)
  An object containing details about the socket’s remote endpoint.
- [class NEFilterFlow](../nefilterflow.md)
  The abstract base class for types that represent flows of network data.
- [var localEndpoint: NWEndpoint?](./localendpoint.md)
  An object containing details about the socket’s local endpoint.
- [var socketFamily: Int32](./socketfamily.md)
  The protocol family of the socket.
- [var socketType: Int32](./sockettype.md)
  The type of the socket.
- [var socketProtocol: Int32](./socketprotocol.md)
  The protocol of the socket.


---

*[View on Apple Developer](https://developer.apple.com/documentation/networkextension/nefiltersocketflow/remotehostname)*