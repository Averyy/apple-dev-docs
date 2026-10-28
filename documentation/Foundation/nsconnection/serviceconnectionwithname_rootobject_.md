# serviceConnectionWithName:rootObject:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a new connection object representing a vended service on the default system port name server.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.13

## Declaration

```objc
+ (instancetype) serviceConnectionWithName:(NSString *) name rootObject:(id) root;
```

## Return Value

An `NSConnection` object representing the vended service or `nil` if there was a problem setting up the connection object.

## Discussion

This method creates the server-side of a connection object and registers it with the default system port name server. Clients wishing to connect to this service can request a communications port from the same port server and use that port to communicate.

## Parameters

- `name`: The name of the service you want to publish.
- `root`: The object to use as the root object for the published service. This is the object vended by the connection.

## See Also

### Related Documentation
- [+ systemDefaultPortNameServer](../nsportnameserver/systemdefaultportnameserver.md)
  Returns the single instance of `NSPortNameServer` for the application.
- [+ connectionWithRegisteredName:host:](./connectionwithregisteredname_host_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
### Vending a Service
- [+ serviceConnectionWithName:rootObject:usingNameServer:](./serviceconnectionwithname_rootobject_usingnameserver_.md)
  Creates and returns a new connection object representing a vended service on the specified port name server.
- [- registerName:](./registername_.md)
  Registers the specified service using with the default system port name server.
- [- registerName:withNameServer:](./registername_withnameserver_.md)
  Registers a service with the specified port name server.
- [rootObject](./rootobject-c.property.md)
  The object that the receiver (or its parent) makes available to other applications or threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/serviceconnectionwithname:rootobject:)*