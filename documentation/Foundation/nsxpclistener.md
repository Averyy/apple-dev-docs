# NSXPCListener

**Framework**: Foundation  
**Kind**: class

A listener that waits for new incoming connections, configures them, and accepts or rejects them.

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
class NSXPCListener
```

#### Overview

Each XPC service, launchd agent, or launchd daemon typically has at least one [`NSXPCListener`](nsxpclistener.md) object that listens for connections to a specified service name. Each listener must have a delegate that conforms to the [`NSXPCListenerDelegate`](nsxpclistenerdelegate.md) protocol. When the listener receives a new connection request, it creates a new [`NSXPCConnection`](nsxpcconnection.md) object, then asks the delegate to inspect, configure, and resume the connection object by calling the delegate’s [`listener(_:shouldAcceptNewConnection:)`](nsxpclistenerdelegate/listener(_:shouldacceptnewconnection:).md) method.

## Topics

### Creating a listener
- [init(machServiceName: String)](nsxpclistener/init(machservicename:).md)
  Initializes a listener in a LaunchAgent or LaunchDaemon which has a name advertised in a `launchd.plist` file.
### Using standard listeners
- [class func service() -> NSXPCListener](nsxpclistener/service.md)
  Returns the singleton listener used to listen for incoming connections in an XPC service.
- [class func anonymous() -> NSXPCListener](nsxpclistener/anonymous.md)
  Returns a new anonymous listener connection.
### Working with a delegate
- [var delegate: (any NSXPCListenerDelegate)?](nsxpclistener/delegate.md)
  The delegate for the listener.
### Providing access to clients
- [var endpoint: NSXPCListenerEndpoint](nsxpclistener/endpoint.md)
  Returns an endpoint object that may be sent over an existing connection.
### Managing connection state
- [func activate()](nsxpclistener/activate.md)
  Activates the listener.
- [func resume()](nsxpclistener/resume.md)
  Starts processing of incoming requests.
- [func invalidate()](nsxpclistener/invalidate.md)
  Invalidates the listener.
- [func suspend()](nsxpclistener/suspend.md)
  Suspends the listener.
### Working with code-signing
- [func setConnectionCodeSigningRequirement(String)](nsxpclistener/setconnectioncodesigningrequirement(_:).md)
  Sets the code signing requirement for connections to this listener.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol NSXPCListenerDelegate](nsxpclistenerdelegate.md)
  The protocol that delegates to the XPC listener use to accept or reject new connections.
- [class NSXPCListenerEndpoint](nsxpclistenerendpoint.md)
  An object that names a specific XPC listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpclistener)*