# init(listenerEndpoint:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](../nsxpclistenerendpoint.md) object.

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
init(listenerEndpoint endpoint: NSXPCListenerEndpoint)
```

```objc
- (instancetype) initWithListenerEndpoint:(NSXPCListenerEndpoint *) endpoint;
```

## Parameters

- `endpoint`: The desired listener endpoint for the service.

## See Also

### Related Documentation
- [Daemons and Services Programming Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
### Creating a connection
- [init(machServiceName: String, options: NSXPCConnection.Options)](./init%28machservicename,options%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [NSXPCConnection.Options](./options.md)
  Options that you can pass to a connection.
- [init(serviceName: String)](./init%28servicename%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in an XPC service, identified by a service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/init(listenerendpoint:))*