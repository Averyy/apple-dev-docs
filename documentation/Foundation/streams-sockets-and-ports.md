# Streams, Sockets, and Ports

**Framework**: Foundation

Use low-level Unix features to manage input and output among files, processes, and the network.

## Topics

### Streams
- [class Stream](stream.md)
  An abstract class representing a stream.
- [class InputStream](inputstream.md)
  A stream that provides read-only stream functionality.
- [class OutputStream](outputstream.md)
  A stream that provides write-only stream functionality.
- [protocol StreamDelegate](streamdelegate.md)
  An interface that delegates of a stream instance use to handle events on the stream.
### Tasks and Pipes
- [class Process](process.md)
  An object that represents a subprocess of the current process.
- [class Pipe](pipe.md)
  A one-way communications channel between related processes.
### Sockets
- [class Host](host.md)
  A representation of an individual host on the network.
- [class Port](port.md)
  An abstract class that represents a communication channel.
- [class SocketPort](socketport.md)
  A port that represents a BSD socket.
### Byte Ordering
- [Byte Order Utilities](byte-order-utilities.md)
  Examine and manage the byte order of numbers communicated through network channels.

## See Also

- [XPC](xpc.md)
  Manage secure interprocess communication.
- [Object Runtime](object-runtime.md)
  Get low-level support for basic Objective-C features, Cocoa design patterns, and Swift integration.
- [Processes and Threads](processes-and-threads.md)
  Manage your app’s interaction with the host operating system and other processes, and implement low-level concurrency features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/streams-sockets-and-ports)*