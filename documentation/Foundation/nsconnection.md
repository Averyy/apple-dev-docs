# NSConnection

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

An object that manages the communication between objects in different threads or between a thread and a process running on a local or remote system.

**Availability**:
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.0+ - Deprecated in 10.13

> **Deprecated**: Use [`NSXPCConnection`](./nsxpcconnection.md) instead.

## Declaration

```objc
@interface NSConnection : NSObject
```

## Overview

Connection objects form the backbone of the distributed objects mechanism and normally operate in the background. You use the methods of [`NSConnection`](./nsconnection.md) explicitly when vending an object to other applications, when accessing such a vended object through a proxy, and when altering default communication parameters. At other times, you simply interact with a vended object or its proxy.

A single connection object may be shared by multiple threads and used to access a vended object.

## Topics

### Getting the Default Instance
- [+ defaultConnection](./nsconnection/defaultconnection.md)
  Returns the default `NSConnection` object for the current thread.
### Creating Instances
- [+ connectionWithReceivePort:sendPort:](./nsconnection/connectionwithreceiveport_sendport_.md)
  Returns an `NSConnection` object that communicates using given send and receive ports.
- [- initWithReceivePort:sendPort:](./nsconnection/initwithreceiveport_sendport_.md)
  Returns an `NSConnection` object initialized with given send and receive ports.
### Running the Connection in a New Thread
- [- runInNewThread](./nsconnection/runinnewthread.md)
  Creates and starts a new `NSThread` object and then runs the receiving connection in the new thread.
- [- enableMultipleThreads](./nsconnection/enablemultiplethreads.md)
  Configures the receiver to allow requests from multiple threads to the remote object, without requiring each thread to each maintain its own connection.
- [multipleThreadsEnabled](./nsconnection/multiplethreadsenabled.md)
  A Boolean value that indicates whether the receiver supports requests from multiple threads.
- [- addRunLoop:](./nsconnection/addrunloop_.md)
  Adds the specified run loop to the list of run loops the receiver monitors and from which it responds to requests.
- [- removeRunLoop:](./nsconnection/removerunloop_.md)
  Removes a given `NSRunLoop` object from the list of run loops the receiver monitors and from which it responds to requests.
### Vending a Service
- [+ serviceConnectionWithName:rootObject:usingNameServer:](./nsconnection/serviceconnectionwithname_rootobject_usingnameserver_.md)
  Creates and returns a new connection object representing a vended service on the specified port name server.
- [+ serviceConnectionWithName:rootObject:](./nsconnection/serviceconnectionwithname_rootobject_.md)
  Creates and returns a new connection object representing a vended service on the default system port name server.
- [- registerName:](./nsconnection/registername_.md)
  Registers the specified service using with the default system port name server.
- [- registerName:withNameServer:](./nsconnection/registername_withnameserver_.md)
  Registers a service with the specified port name server.
- [rootObject](./nsconnection/rootobject-c.property.md)
  The object that the receiver (or its parent) makes available to other applications or threads.
### Getting a Remote Object
- [+ connectionWithRegisteredName:host:](./nsconnection/connectionwithregisteredname_host_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ connectionWithRegisteredName:host:usingNameServer:](./nsconnection/connectionwithregisteredname_host_usingnameserver_.md)
  Returns the `NSConnection` object whose send port links it to the `NSConnection` object registered under a given name with a given server on a given host.
- [rootProxy](./nsconnection/rootproxy.md)
  The proxy for the root object of the receiver’s peer in another application or thread.
- [+ rootProxyForConnectionWithRegisteredName:host:](./nsconnection/rootproxyforconnectionwithregisteredname_host_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with the default `NSPortNameServer` under a given name on a given host.
- [+ rootProxyForConnectionWithRegisteredName:host:usingNameServer:](./nsconnection/rootproxyforconnectionwithregisteredname_host_usingnameserver_.md)
  Returns a proxy for the root object of the `NSConnection` object registered with `server` under `name` on a given host.
- [remoteObjects](./nsconnection/remoteobjects.md)
  The local proxies for remote objects that have been received over the connection but not deallocated yet.
- [localObjects](./nsconnection/localobjects.md)
  The local objects that have been sent over the connection and still have proxies at the other end.
### Getting a Conversation
- [+ currentConversation](./nsconnection/currentconversation.md)
  Returns a token object representing any conversation in progress in the current thread.
### Getting All NSConnection Objects
- [+ allConnections](./nsconnection/allconnections.md)
  Returns all valid `NSConnection` objects in the process.
### Configuring Instances
- [requestTimeout](./nsconnection/requesttimeout.md)
  The timeout interval for outgoing remote messages.
- [replyTimeout](./nsconnection/replytimeout.md)
  The timeout interval for replies to outgoing remote messages.
- [independentConversationQueueing](./nsconnection/independentconversationqueueing.md)
  A Boolean value that indicates whether the receiver handles remote messages atomically.
- [- addRequestMode:](./nsconnection/addrequestmode_.md)
  Adds `mode` to the set of run-loop input modes that the receiver uses for connection requests.
- [- removeRequestMode:](./nsconnection/removerequestmode_.md)
  Removes `mode` from the set of run-loop input modes the receiver uses for connection requests.
- [requestModes](./nsconnection/requestmodes-c.property.md)
  The set of request modes the receiver’s receive port is registered for with its `NSRunLoop` object.
- [- invalidate](./nsconnection/invalidate.md)
  Invalidates the receiver.
- [valid](./nsconnection/valid.md)
  A Boolean value that indicates whether the receiver is known to be valid.
### Getting Ports
- [receivePort](./nsconnection/receiveport-c.property.md)
  The port on which the receiver receives incoming network messages.
- [sendPort](./nsconnection/sendport-c.property.md)
  The port that the connection sends outgoing network messages through.
- [- dispatchWithComponents:](./nsconnection/dispatchwithcomponents_.md)
  Allows subclasses to ask a connection object to dispatch component data.
### Getting Statistics
- [statistics](./nsconnection/statistics-c.property.md)
  A dictionary containing various statistics for the receiver.
### Setting the Delegate
- [delegate](./nsconnection/delegate-c.property.md)
  The receiver’s delegate.
### Constants
- [NSConnection run loop mode](./nsconnection-run-loop-mode.md)
  `NSConnection` defines the following run loop mode—see [`RunLoop`](./runloop.md) for more details.
- [Connection Exception Names](./connection-exception-names.md)
  The name of an exception raised in case of authentication failure.
### Notifications
- [NSConnectionDidDieNotification](./nsconnectiondiddienotification.md)
  Posted when an `NSConnection` object is deallocated or when it’s notified that its `NSPort` object has become invalid. The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.
- [NSConnectionDidInitializeNotification](./nsconnectiondidinitializenotification.md)
  Posted when an `NSConnection` object is initialized using [`initWithReceivePort:sendPort:`](./nsconnection/initwithreceiveport_sendport_.md) (the designated initializer for `NSConnection`). The notification object is the `NSConnection` object. This notification does not contain a `userInfo` dictionary.
### Instance Variables
- [authCheck](./nsconnection/authcheck.md)
- [authGen](./nsconnection/authgen.md)
- [busy](./nsconnection/busy.md)
- [classInfoImported](./nsconnection/classinfoimported.md)
- [delayedRL](./nsconnection/delayedrl.md)
- [delegate](./nsconnection/delegate-c.ivar.md)
- [doRequest](./nsconnection/dorequest.md)
- [invalidateRP](./nsconnection/invalidaterp.md)
- [isDead](./nsconnection/isdead.md)
- [isMulti](./nsconnection/ismulti.md)
- [isQueueing](./nsconnection/isqueueing.md)
- [isValid](./nsconnection/isvalid.md)
- [localProxyCount](./nsconnection/localproxycount.md)
- [receivePort](./nsconnection/receiveport-c.ivar.md)
- [registerInfo](./nsconnection/registerinfo.md)
- [releasedProxies](./nsconnection/releasedproxies.md)
- [replMode](./nsconnection/replmode.md)
- [requestModes](./nsconnection/requestmodes-c.ivar.md)
- [reserved](./nsconnection/reserved.md)
- [rootObject](./nsconnection/rootobject-c.ivar.md)
- [runLoops](./nsconnection/runloops.md)
- [sendPort](./nsconnection/sendport-c.ivar.md)
- [statistics](./nsconnection/statistics-c.ivar.md)
- [waitCount](./nsconnection/waitcount.md)
- [wantsInvalid](./nsconnection/wantsinvalid.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Legacy
- [protocol NSMachPortDelegate](./nsmachportdelegate.md)
  An interface for handling incoming Mach messages.
- [NSConnectionDelegate](./nsconnectiondelegate.md)
  An interface for interacting with low-level, interprocess connections.
- [NSDistantObject](./nsdistantobject.md)
  A proxy for objects in other applications or threads.
- [NSDistantObjectRequest](./nsdistantobjectrequest.md)
  An object used by the distributed objects system to help handle invocations between different processes.
- [NSMachBootstrapServer](./nsmachbootstrapserver.md)
  A port name server that takes and returns Mach port objects.
- [class NSMachPort](./nsmachport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [class MessagePort](./messageport.md)
  A port that can be used as an endpoint for distributed object connections (or raw messaging).
- [NSMessagePortNameServer](./nsmessageportnameserver.md)
  A server takes and returns message ports.
- [NSPortCoder](./nsportcoder.md)
  A coder used to transmit object proxies (and sometimes objects themselves) between connections.
- [protocol PortDelegate](./portdelegate.md)
  An interface for handling incoming messages.
- [class PortMessage](./portmessage.md)
  A low-level, operating system-independent type for inter-application (and inter-thread) messages.
- [NSPortNameServer](./nsportnameserver.md)
  An object-oriented interface to the port registration service used by the distributed objects system.
- [class NSProtocolChecker](./nsprotocolchecker.md)
  An object that restricts the messages that can be sent to another object (referred to as the checker’s delegate).
- [NSSocketPortNameServer](./nssocketportnameserver.md)
  A port name server that takes and returns socket ports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsconnection)*