# XPC

**Framework**: Foundation

Manage secure interprocess communication.

## Topics

### XPC Client
- [protocol NSXPCProxyCreating](nsxpcproxycreating.md)
  Methods for creating new proxy objects.
- [class NSXPCConnection](nsxpcconnection.md)
  A bidirectional communication channel between two processes.
- [class NSXPCInterface](nsxpcinterface.md)
  An interface that may be sent to an exported object or remote object proxy.
- [class NSXPCCoder](nsxpccoder.md)
  A coder that encodes and decodes objects that your app sends over an XPC connection.
### XPC Services
- [class NSXPCListener](nsxpclistener.md)
  A listener that waits for new incoming connections, configures them, and accepts or rejects them.
- [protocol NSXPCListenerDelegate](nsxpclistenerdelegate.md)
  The protocol that delegates to the XPC listener use to accept or reject new connections.
- [class NSXPCListenerEndpoint](nsxpclistenerendpoint.md)
  An object that names a specific XPC listener.

## See Also

- [Object Runtime](object-runtime.md)
  Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](processes-and-threads.md)
  Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.
- [Streams, Sockets, and Ports](streams-sockets-and-ports.md)
  Use low-level Unix features to manage input and output among files, processes, and the network.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/xpc)*