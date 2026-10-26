# rootObject

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The object that the receiver (or its parent) makes available to other applications or threads.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (retain, nullable) id rootObject;
```

#### Discussion

The object that the receiver (or its parent) makes available to other applications or threads, or `nil` if there is no root object.

To get a proxy to this object in another application or thread, invoke the [`rootProxyForConnectionWithRegisteredName:host:`](./rootproxyforconnectionwithregisteredname_host_.md) class method with the appropriate arguments.

Changing the root object only affects new connection requests and [`rootProxy`](./rootproxy.md) messages to established `NSConnection` objects—applications that have proxies to the old root object can still send messages through it.

## See Also

### Related Documentation
- [rootProxy](./rootproxy.md)
  The proxy for the root object of the receiver’s peer in another application or thread.
### Vending a Service
- [+ serviceConnectionWithName:rootObject:usingNameServer:](./serviceconnectionwithname_rootobject_usingnameserver_.md)
  Creates and returns a new connection object representing a vended service on the specified port name server.
- [+ serviceConnectionWithName:rootObject:](./serviceconnectionwithname_rootobject_.md)
  Creates and returns a new connection object representing a vended service on the default system port name server.
- [- registerName:](./registername_.md)
  Registers the specified service using with the default system port name server.
- [- registerName:withNameServer:](./registername_withnameserver_.md)
  Registers a service with the specified port name server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/rootobject-c.property)*