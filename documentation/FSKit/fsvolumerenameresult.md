# FSVolumeRenameResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of a rename-volume call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSVolumeRenameResult
```

```objc
@interface FSVolumeRenameResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`setVolumeName(_:context:replyHandler:)`](./fsvolume/renamehandler/setvolumename%28_,context,replyhandler%29.md).

## Topics

### Creating a volume-rename result
- [init?(newName: FSFileName)](./fsvolumerenameresult/init%28newname%29.md)
  Creates a result for a volume-renaming operation.
- [class FSFileName](./fsfilename.md)
  The name of a file, expressed as a data buffer.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](./fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Renaming the volume
- [func setVolumeName(FSFileName, context: FSContext, replyHandler: (FSVolumeRenameResult?, (any Error)?) -> Void)](./fsvolume/renamehandler/setvolumename%28_,context,replyhandler%29.md)
  Sets a new name for the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumerenameresult)*