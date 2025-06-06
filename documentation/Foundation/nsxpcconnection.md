# NSXPCConnection

**Framework**: Foundation  
**Kind**: class

A bidirectional communication channel between two processes.

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
class NSXPCConnection
```

#### Overview

This class is the primary means of creating and configuring the communication mechanism between two processes. Each process has one instance of this class to represent the endpoint in the communication channel.

## Topics

### Creating a connection
- [init(listenerEndpoint: NSXPCListenerEndpoint)](nsxpcconnection/init(listenerendpoint:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in another process, identified by an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object.
- [init(machServiceName: String, options: NSXPCConnection.Options)](nsxpcconnection/init(machservicename:options:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to a LaunchAgent or LaunchDaemon with a name advertised in a `launchd.plist`.
- [NSXPCConnection.Options](nsxpcconnection/options.md)
  Options that you can pass to a connection.
- [init(serviceName: String)](nsxpcconnection/init(servicename:).md)
  Initializes an [`NSXPCConnection`](nsxpcconnection.md) object to connect to an [`NSXPCListener`](nsxpclistener.md) object in an XPC service, identified by a service name.
### Managing connection state
- [func activate()](nsxpcconnection/activate.md)
  Activates the connection.
- [func resume()](nsxpcconnection/resume.md)
  Starts or resumes handling of messages on a connection.
- [func invalidate()](nsxpcconnection/invalidate.md)
  Invalidates the connection.
- [func suspend()](nsxpcconnection/suspend.md)
  Suspends the connection.
- [var interruptionHandler: (() -> Void)?](nsxpcconnection/interruptionhandler.md)
  An interruption handler that is called if the remote process exits or crashes.
- [var invalidationHandler: (() -> Void)?](nsxpcconnection/invalidationhandler.md)
  An invalidation handler that is called if the connection can not be formed or the connection has terminated and may not be re-established.
- [class func current() -> NSXPCConnection?](nsxpcconnection/current.md)
  Returns the current connection, in the context of a call to a method on your exported object.
- [func scheduleSendBarrierBlock(() -> Void)](nsxpcconnection/schedulesendbarrierblock(_:).md)
  Add a barrier block to execute on the connection.
### Managing the connection interface
- [var serviceName: String?](nsxpcconnection/servicename.md)
  The name of the XPC service that this connection was configured to connect to.
- [var endpoint: NSXPCListenerEndpoint](nsxpcconnection/endpoint.md)
  If the connection was created with an [`NSXPCListenerEndpoint`](nsxpclistenerendpoint.md) object, returns the endpoint object used.
- [var exportedInterface: NSXPCInterface?](nsxpcconnection/exportedinterface.md)
  The [`NSXPCInterface`](nsxpcinterface.md) object that describes the protocol for the exported object on this connection.
- [var exportedObject: Any?](nsxpcconnection/exportedobject.md)
  An exported object for the connection.
- [var remoteObjectInterface: NSXPCInterface?](nsxpcconnection/remoteobjectinterface.md)
  Defines the [`NSXPCInterface`](nsxpcinterface.md) object that describes the protocol for the object represented by the `remoteObjectProxy`.
- [var remoteObjectProxy: Any](nsxpcconnection/remoteobjectproxy.md)
  Returns a proxy for the remote object (that is, the `exportedObject` from the other side of this connection).
### Working with security attributes
- [var auditSessionIdentifier: au_asid_t](nsxpcconnection/auditsessionidentifier.md)
  The BSM audit session identifier for the connecting process.
- [var processIdentifier: pid_t](nsxpcconnection/processidentifier.md)
  The process ID (PID) of the connecting process.
- [var effectiveGroupIdentifier: gid_t](nsxpcconnection/effectivegroupidentifier.md)
  The effective group ID (EGID) of the connecting process.
- [var effectiveUserIdentifier: uid_t](nsxpcconnection/effectiveuseridentifier.md)
  The effective user ID (EUID) of the connecting process.
### Working with proxy objects
- [func remoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcconnection/remoteobjectproxywitherrorhandler(_:).md)
  Returns a proxy for the remote object (that is, the object exported from the other side of this connection) with the specified error handler.
- [func synchronousRemoteObjectProxyWithErrorHandler((any Error) -> Void) -> Any](nsxpcconnection/synchronousremoteobjectproxywitherrorhandler(_:).md)
### Working with code signing
- [func setCodeSigningRequirement(String)](nsxpcconnection/setcodesigningrequirement(_:).md)
  Sets the code signing requirement for this connection.
### Error codes
- [var NSXPCConnectionInterrupted: Int](nsxpcconnectioninterrupted-swift.var.md)
  The XPC connection was interrupted.
- [var NSXPCConnectionInvalid: Int](nsxpcconnectioninvalid-swift.var.md)
  The XPC connection was invalid.
- [var NSXPCConnectionReplyInvalid: Int](nsxpcconnectionreplyinvalid-swift.var.md)
  The XPC connection reply was invalid.
- [var NSXPCConnectionErrorMinimum: Int](nsxpcconnectionerrorminimum-swift.var.md)
  The lower bounds of XPC connection error code values.
- [var NSXPCConnectionErrorMaximum: Int](nsxpcconnectionerrormaximum-swift.var.md)
  The upper bounds of XPC connection error code values.
- [var NSXPCConnectionCodeSigningRequirementFailure: Int](nsxpcconnectioncodesigningrequirementfailure-swift.var.md)
  A code-signing requirement check failed.

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
- [NSXPCProxyCreating](nsxpcproxycreating.md)

## See Also

- [protocol NSXPCProxyCreating](nsxpcproxycreating.md)
  Methods for creating new proxy objects.
- [class NSXPCInterface](nsxpcinterface.md)
  An interface that may be sent to an exported object or remote object proxy.
- [class NSXPCCoder](nsxpccoder.md)
  A coder that encodes and decodes objects that your app sends over an XPC connection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsxpcconnection)*