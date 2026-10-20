# NSXPCConnection.Options

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

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

```c
enum NSXPCConnectionOptions : NSUInteger;
```

## Topics

### Constants
- [static var privileged: NSXPCConnection.Options](./options/privileged.md)
### Initializers
- [init(rawValue: UInt)](./options/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)

## See Also

### Creating a connection
- [init(listenerEndpoint: NSXPCListenerEndpoint)](./init%28listenerendpoint%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](../nsxpclistenerendpoint.md) object.
- [init(machServiceName: String, options: NSXPCConnection.Options)](./init%28machservicename,options%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [init(serviceName: String)](./init%28servicename%29.md)
  Initializes an [`NSXPCConnection`](../nsxpcconnection.md) object to connect to an [`NSXPCListener`](../nsxpclistener.md) object in an XPC service, identified by a service name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection/options)*