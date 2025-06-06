# init(listenerEndpoint:)

**Framework**: Foundation  
**Kind**: init

Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object.

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

## Parameters

- `endpoint`: The desired listener endpoint for the service.

## See Also

- [Daemons and Services Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/Introduction.html#//apple_ref/doc/uid/10000172i)
- [init(machServiceName: String, options: NSXPCConnection.Options)](nsxpcconnection/init(machservicename:options:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [NSXPCConnection.Options](nsxpcconnection/options.md)
  Options that you can pass to a connection.
- [init(serviceName: String)](nsxpcconnection/init(servicename:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in an XPC service, identified by a service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/init(listenerendpoint:))*