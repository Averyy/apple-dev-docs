# connectionWithRegisteredName:host:usingNameServer:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (instancetype) connectionWithRegisteredName:(NSString *) name host:(NSString *) hostName usingNameServer:(NSPortNameServer *) server;
```

## Return Value

The `NSConnection` object whose send port links it to the `NSConnection` object registered with `server` under `name` on the host named `hostName`.

## Discussion

See [`connectionWithRegisteredName:host:`](./connectionwithregisteredname_host_.md) for more information.

## Parameters

- `name`: The connection name.
- `hostName`: The host name.
- `server`: The name server.

## See Also

### Getting a Remote Object
- [+ connectionWithRegisteredName:host:](./connectionwithregisteredname_host_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [rootProxy](./rootproxy.md)
  The proxy for the root object of the receiver’s peer in another application or thread.
- [+ rootProxyForConnectionWithRegisteredName:host:](./rootproxyforconnectionwithregisteredname_host_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ rootProxyForConnectionWithRegisteredName:host:usingNameServer:](./rootproxyforconnectionwithregisteredname_host_usingnameserver_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host.
- [remoteObjects](./remoteobjects.md)
  The local proxies for remote objects that have been received over the connection but not deallocated yet.
- [localObjects](./localobjects.md)
  The local objects that have been sent over the connection and still have proxies at the other end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/connectionwithregisteredname:host:usingnameserver:)*