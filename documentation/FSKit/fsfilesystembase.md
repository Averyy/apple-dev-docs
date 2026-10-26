# FSFileSystemBase

**Framework**: FSKit  
**Kind**: protocol  
**Role**: Protocol

A protocol containing functionality supplied by FSKit to file system implementations.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSFileSystemBase : NSObjectProtocol
```

```objc
@protocol FSFileSystemBase <NSObject>
```

#### Overview

Both [`FSFileSystem`](./fsfilesystem.md) and [`FSUnaryFileSystem`](./fsunaryfilesystem.md) conform to this protocol.

## Topics

### Implementing essential functionality
- [var containerStatus: FSContainerStatus](./fsfilesystembase/containerstatus.md)
  The status of the file system container, indicating its readiness and activity.
- [func wipe(FSBlockDeviceResource, completionHandler: ((any Error)?) -> Void)](./fsfilesystembase/wipe%28_,completionhandler%29.md)
  Wipes existing file systems on the specified resource.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Conforming Types
- [FSUnaryFileSystem](./fsunaryfilesystem.md)
- [FSFileSystem](./fsfilesystem.md)

## See Also

### File systems
- [class FSUnaryFileSystem](./fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.
- [FSFileSystem](./fsfilesystem.md)
  An abstract base class for implementing a full-featured file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystembase)*