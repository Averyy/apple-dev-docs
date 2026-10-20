# remoteObjectProxy

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var remoteObjectProxy: Any { get }
```

```objc
@property (retain, readonly) id remoteObjectProxy;
```

#### Discussion

See descriptions in [`NSXPCProxyCreating`](../nsxpcproxycreating.md) for more details.

## See Also

### Managing the connection interface
- [var serviceName: String?](./servicename.md)
  The name of the XPC service that this connection was configured to connect to.
- [var endpoint: NSXPCListenerEndpoint](./endpoint.md)
  If the connection was created with an [`NSXPCListenerEndpoint`](../nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [var exportedInterface: NSXPCInterface?](./exportedinterface.md)
  The [`NSXPCInterface`](../nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [var exportedObject: Any?](./exportedobject.md)
  An exported object for the connection.
- [var remoteObjectInterface: NSXPCInterface?](./remoteobjectinterface.md)
  Defines the [`NSXPCInterface`](../nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/remoteobjectproxy)*