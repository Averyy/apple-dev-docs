# FSFileSystemBase

**Framework**: FSKit  
**Kind**: protocol

A protocol containing functionality supplied by FSKit to file system implementations.

**Availability**:
- macOS 15.4+

## Declaration

```swift
protocol FSFileSystemBase : NSObjectProtocol
```

#### Overview

Both [`FSFileSystem`](fsfilesystem.md) and [`FSUnaryFileSystem`](fsunaryfilesystem.md) conform to this protocol.

## Topics

### Implementing essential functionality
- [var containerStatus: FSContainerStatus](fsfilesystembase/containerstatus.md)
  The status of the file system container, indicating its readiness and activity.
- [func wipe(FSBlockDeviceResource, completionHandler: ((any Error)?) -> Void)](fsfilesystembase/wipe(_:completionhandler:).md)
  Wipes existing file systems on the specified resource.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Conforming Types
- [FSUnaryFileSystem](fsunaryfilesystem.md)

## See Also

- [class FSUnaryFileSystem](fsunaryfilesystem.md)
  An abstract base class for implementing a minimal file system.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystembase)*