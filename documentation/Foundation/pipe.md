# Pipe

**Framework**: Foundation  
**Kind**: class

A one-way communications channel between related processes.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class Pipe
```

#### Overview

[`Pipe`](pipe.md) objects provide an object-oriented interface for accessing pipes. An [`Pipe`](pipe.md) object represents both ends of a pipe and enables communication through the pipe. A pipe is a one-way communications channel between related processes; one process writes data, while the other process reads that data. The data that passes through the pipe is buffered; the size of the buffer is determined by the underlying operating system. [`Pipe`](pipe.md) is an abstract class, the public interface of a class cluster.

## Topics

### Getting the File Handles for a Pipe
- [var fileHandleForReading: FileHandle](pipe/filehandleforreading.md)
  The receiver’s read file handle.
- [var fileHandleForWriting: FileHandle](pipe/filehandleforwriting.md)
  The receiver’s write file handle.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class Process](process.md)
  An object that represents a subprocess of the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/pipe)*