# registerName:

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Registers the specified service using with the default system port name server.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
- (BOOL) registerName:(NSString *) name;
```

## Return Value

[`true`](../../Swift/true.md) if the operation was successful, otherwise [`false`](../../Swift/false.md) (for example, if another `NSConnection` object on the same host is already registered under `name`).

## Discussion

This method connects the receive port of the receiving `NSConnection` object with the specified service name. It registers the name using the port name server returned by the [`systemDefaultPortNameServer`](../nsportnameserver/systemdefaultportnameserver.md) method of `NSPortNameServer`. If the operation is successful, other `NSConnection` objects can contact the receiver using the [`connectionWithRegisteredName:host:`](./connectionwithregisteredname_host_.md) and [`rootProxyForConnectionWithRegisteredName:host:`](./rootproxyforconnectionwithregisteredname_host_.md) class methods.

If the receiver was already registered under a name and this method returns [`false`](../../Swift/false.md), the old name remains in effect. If this method is successful, it also unregisters the old name.

To unregister an `NSConnection` object, simply invoke [`registerName:`](./registername_.md) and supply `nil` as the connection name. Unregistering is currently only supported for [`SocketPort`](../socketport.md)-based connections.

## Parameters

- `name`: The name under which to register the receiver.

## See Also

### Related Documentation
- [+ systemDefaultPortNameServer](../nsportnameserver/systemdefaultportnameserver.md)
  Returns the single instance of `NSPortNameServer` for the application.
### Vending a Service
- [+ serviceConnectionWithName:rootObject:usingNameServer:](./serviceconnectionwithname_rootobject_usingnameserver_.md)
  Creates and returns a new connection object representing a vended service on the specified port name server.
- [+ serviceConnectionWithName:rootObject:](./serviceconnectionwithname_rootobject_.md)
  Creates and returns a new connection object representing a vended service on the default system port name server.
- [- registerName:withNameServer:](./registername_withnameserver_.md)
  Registers a service with the specified port name server.
- [rootObject](./rootobject-c.property.md)
  The object that the receiver (or its parent) makes available to other applications or threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/registername:)*