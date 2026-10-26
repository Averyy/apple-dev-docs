# localObjects

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The local objects that have been sent over the connection and still have proxies at the other end.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

## Declaration

```objc
@property (copy, readonly) NSArray * localObjects;
```

#### Discussion

When an object’s remote proxy is deallocated, a message is sent back to the receiver to notify it that the local object is no longer shared over the connection.

## See Also

### Getting a Remote Object
- [+ connectionWithRegisteredName:host:](./connectionwithregisteredname_host_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ connectionWithRegisteredName:host:usingNameServer:](./connectionwithregisteredname_host_usingnameserver_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.
- [rootProxy](./rootproxy.md)
  The proxy for the root object of the receiver’s peer in another application or thread.
- [+ rootProxyForConnectionWithRegisteredName:host:](./rootproxyforconnectionwithregisteredname_host_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ rootProxyForConnectionWithRegisteredName:host:usingNameServer:](./rootproxyforconnectionwithregisteredname_host_usingnameserver_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host.
- [remoteObjects](./remoteobjects.md)
  The local proxies for remote objects that have been received over the connection but not deallocated yet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection/localobjects)*