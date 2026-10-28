# FSFileSystem

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

An abstract base class for implementing a full-featured file system.

## Declaration

```objc
@interface FSFileSystem : NSObject
```

## Overview

`FSFileSystem` is a full-featured file system, which works with one or more [`FSResource`](./fsresource.md) instances and presents one or more [`FSVolume`](./fsvolume.md) references to callers.

Implement your app extension by providing a subclass of `FSFileSystem` as a delegate object. Your delegate also needs to implement the `FSFileSystemOperations` protocol so that it can probe, load, and unload resources.

> **Note**: The current version of FSKit supports only [`FSUnaryFileSystem`](./fsunaryfilesystem.md), not `FSFileSystem`.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [FSFileSystemBase](./fsfilesystembase.md)

## See Also

### File systems
- [class FSUnaryFileSystem](./fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [protocol FSFileSystemBase](./fsfilesystembase.md)
  A protocol containing functionality supplied by FSKit to file system implementations.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystem)*