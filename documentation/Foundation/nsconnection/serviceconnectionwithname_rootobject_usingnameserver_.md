# serviceConnectionWithName:rootObject:usingNameServer:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Creates and returns a new connection object representing a vended service on the specified port name server.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.5+ - Deprecated in 10.13

## Declaration

```objc
+ (instancetype) serviceConnectionWithName:(NSString *) name rootObject:(id) root usingNameServer:(NSPortNameServer *) server;
```

#### Return Value

An `NSConnection` object representing the vended service or `nil` if there was a problem setting up the connection object.

#### Discussion

This method creates the server-side of a connection object and registers it with the specified port name server. Clients wishing to connect to this service can request a communications port from the same port server and use that port to communicate.

If the specified service name corresponds to a service that is autolaunched by `launchd`, this method allows the service to check in with the `launchd` process. If the service is not autolaunched by `launchd`, this method registers the new connection with the specified name. For more information about `launchd` and its role in launching services, see [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)

## Parameters

- `name`: The name of the service you want to publish.
- `root`: The object to use as the root object for the published service. This is the object vended by the connection.
- `server`: The port name server with which to register your service.

## See Also

### Related Documentation
- [+ connectionWithRegisteredName:host:usingNameServer:](./connectionwithregisteredname_host_usingnameserver_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.
### Vending a Service
- [+ serviceConnectionWithName:rootObject:](./serviceconnectionwithname_rootobject_.md)
  Creates and returns a new connection object representing a vended service on the default system port name server.
- [- registerName:](./registername_.md)
  Registers the specified service using with the default system port name server.
- [- registerName:withNameServer:](./registername_withnameserver_.md)
  Registers a service with the specified port name server.
- [rootObject](./rootobject-c.property.md)
  The object that the receiver (or its parent) makes available to other applications or threads.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/serviceconnectionwithname:rootobject:usingnameserver:)*