# init(machServiceName:options:)

**Framework**: Foundation  
**Kind**: init

Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.

**Availability**:
- macOS 10.8+

## Declaration

```swift
init(machServiceName name: String, options: NSXPCConnection.Options = [])
```

#### Discussion

For example, if an agent is managed with `launchd` and has a `launchd.plist` in `~/Library/LaunchAgents`, this method would create a connection to that agent. The agent should use [`NSXPCListener`](nsxpclistener.md) to wait for new connections.

If the connection is being made to a process that is running in a privileged Mach bootstrap context (for example, a daemon started by a `launchd` property list in `/Library/LaunchDaemons`), then pass the [`NSXPCConnection`](nsxpcconnection.md) option.

## See Also

- [init(listenerEndpoint: NSXPCListenerEndpoint)](nsxpcconnection/init(listenerendpoint:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object.
- [NSXPCConnection.Options](nsxpcconnection/options.md)
  Options that you can pass to a connection.
- [init(serviceName: String)](nsxpcconnection/init(servicename:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in an XPC service, identified by a service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/init(machservicename:options:))*