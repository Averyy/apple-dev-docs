# init(serviceName:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in an XPC service, identified by a service name.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(serviceName: String)
```

```objc
- (instancetype) initWithServiceName:(NSString *) serviceName;
```

## Discussion

XPC services are helper processes that are usually part of your application bundle. The service should use [`NSXPCListener`](../nsxpclistener.md) to wait for new connections.

## See Also

### Creating a connection
- [init(listenerEndpoint: NSXPCListenerEndpoint)](./init%28listenerendpoint%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](../nsxpclistenerendpoint.md) object.
- [init(machServiceName: String, options: NSXPCConnection.Options)](./init%28machservicename,options%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [NSXPCConnection.Options](./options.md)
  Options that you can pass to a connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/init(servicename:))*