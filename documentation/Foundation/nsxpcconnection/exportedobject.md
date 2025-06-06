# exportedObject

**Framework**: Foundation  
**Kind**: property

An exported object for the connection.

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
var exportedObject: Any? { get set }
```

#### Discussion

Messages sent to the [`remoteObjectProxy()`](nsxpcproxycreating/remoteobjectproxy().md) object from the other side of the connection are dispatched to this object. Messages delivered to exported objects are serialized and sent on a non-main queue. The receiver is responsible for handling the messages on a different queue or thread if it is required.

## See Also

- [var serviceName: String?](nsxpcconnection/servicename.md)
  The name of the XPC service that this connection was configured to connect to.
- [var endpoint: NSXPCListenerEndpoint](nsxpcconnection/endpoint.md)
  If the connection was created with an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [var exportedInterface: NSXPCInterface?](nsxpcconnection/exportedinterface.md)
  The [`NSXPCInterface`](nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [var remoteObjectInterface: NSXPCInterface?](nsxpcconnection/remoteobjectinterface.md)
  Defines the [`NSXPCInterface`](nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [var remoteObjectProxy: Any](nsxpcconnection/remoteobjectproxy.md)
  Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/exportedobject)*