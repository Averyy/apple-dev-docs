# Pipe

**Framework**: Foundation  
**Kind**: class  
**Role**: Class

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

```objc
@interface NSPipe : NSObject
```

## Overview

[`Pipe`](./pipe.md) objects provide an object-oriented interface for accessing pipes. An [`Pipe`](./pipe.md) object represents both ends of a pipe and enables communication through the pipe. A pipe is a one-way communications channel between related processes; one process writes data, while the other process reads that data. The data that passes through the pipe is buffered; the size of the buffer is determined by the underlying operating system. [`Pipe`](./pipe.md) is an abstract class, the public interface of a class cluster.

## Topics

### Getting the File Handles for a Pipe
- [var fileHandleForReading: FileHandle](./pipe/filehandleforreading.md)
  The receiver’s read file handle.
- [var fileHandleForWriting: FileHandle](./pipe/filehandleforwriting.md)
  The receiver’s write file handle.
### Creating an NSPipe Object
- [+ pipe](./nspipe/pipe.md)
  Returns an `NSPipe` object.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Tasks and Pipes
- [class Process](./process.md)
  An object that represents a subprocess of the current process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/pipe)*