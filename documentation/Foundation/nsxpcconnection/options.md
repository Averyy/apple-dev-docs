# NSXPCConnection.Options

**Framework**: Foundation  
**Kind**: struct

Options that you can pass to a connection.

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
struct Options
```

## Topics

### Constants
- [static var privileged: NSXPCConnection.Options](nsxpcconnection/options/privileged.md)
- [static var privileged: NSXPCConnection.Options](nsxpcconnection/options/privileged.md)
### Initializers
- [init(rawValue: UInt)](nsxpcconnection/options/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [init(listenerEndpoint: NSXPCListenerEndpoint)](nsxpcconnection/init(listenerendpoint:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object.
- [init(machServiceName: String, options: NSXPCConnection.Options)](nsxpcconnection/init(machservicename:options:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [init(serviceName: String)](nsxpcconnection/init(servicename:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in an XPC service, identified by a service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/options)*