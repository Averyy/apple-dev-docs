# FSUnaryFileSystem

**Framework**: FSKit  
**Kind**: class

An abstract base class for implementing a minimal file system.

**Availability**:
- macOS 15.4+

## Declaration

```swift
class FSUnaryFileSystem
```

#### Overview

`FSUnaryFileSystem` is a simplified file system, which works with one [`FSResource`](fsresource.md) and presents it as one [`FSVolume`](fsvolume.md).

The one volume and its container have a shared state and lifetime, a more constrained life cycle than the [`FSFileSystem`](fsfilesystem.md) design flow.

Implement your app extension by providing a subclass of `FSUnaryFileSystem` as a delegate object. Your delegate also needs to implement the [`FSUnaryFileSystemOperations`](fsunaryfilesystemoperations.md) protocol so that it can load resources.

## Topics

### Implementing operations
- [protocol FSUnaryFileSystemOperations](fsunaryfilesystemoperations.md)
  Operations performed by a unary file system.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [FSFileSystemBase](fsfilesystembase.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [protocol FSFileSystemBase](fsfilesystembase.md)
  A protocol containing functionality supplied by FSKit to file system implementations.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsunaryfilesystem)*