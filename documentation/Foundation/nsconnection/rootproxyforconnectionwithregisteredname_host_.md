# rootProxyForConnectionWithRegisteredName:host:

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
+ (NSDistantObject *) rootProxyForConnectionWithRegisteredName:(NSString *) name host:(NSString *) hostName;
```

## Return Value

A proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under `name` on the host named `hostName`, or `nil` if that `NSConnection` object has no root object set. Also returns `nil` if no `NSConnection` object can be found for `name` and `hostName`.

## Discussion

The `NSConnection` object of the returned proxy is a child of the default `NSConnection` object for the current thread (that is, it shares the default `NSConnection` object’s receive port).

This method invokes [`connectionWithRegisteredName:host:`](./connectionwithregisteredname_host_.md) and sends the resulting `NSConnection` object a [`rootProxy`](./rootproxy.md) message.

## Parameters

- `name`: The name under which the connection is registered.
- `hostName`: The host name. The domain name `hostName` is an Internet domain name (for example, `"sales.anycorp.com"`). If `hostName` is `nil` or empty, then only the local host is searched for the named `NSConnection` object.

## See Also

### Related Documentation
- [rootObject](./rootobject-c.property.md)
  The object that the receiver (or its parent) makes available to other applications or threads.
### Getting a Remote Object
- [+ connectionWithRegisteredName:host:](./connectionwithregisteredname_host_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ connectionWithRegisteredName:host:usingNameServer:](./connectionwithregisteredname_host_usingnameserver_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.
- [rootProxy](./rootproxy.md)
  The proxy for the root object of the receiver’s peer in another application or thread.
- [+ rootProxyForConnectionWithRegisteredName:host:usingNameServer:](./rootproxyforconnectionwithregisteredname_host_usingnameserver_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host.
- [remoteObjects](./remoteobjects.md)
  The local proxies for remote objects that have been received over the connection but not deallocated yet.
- [localObjects](./localobjects.md)
  The local objects that have been sent over the connection and still have proxies at the other end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/rootproxyforconnectionwithregisteredname:host:)*