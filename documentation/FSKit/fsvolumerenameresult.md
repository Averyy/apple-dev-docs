# FSVolumeRenameResult

**Framework**: FSKit  
**Kind**: class

The result of a rename-volume call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSVolumeRenameResult
```

#### Overview

Use this type in your implementation of [`setVolumeName(_:context:replyHandler:)`](fsvolume/renamehandler/setvolumename(_:context:replyhandler:).md).

## Topics

### Creating a volume-rename result
- [init?(newName: FSFileName)](fsvolumerenameresult/init(newname:).md)
  Creates a result for a volume-renaming operation.
- [class FSFileName](fsfilename.md)
  The name of a file, expressed as a data buffer.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func setVolumeName(FSFileName, context: FSContext, replyHandler: (FSVolumeRenameResult?, (any Error)?) -> Void)](fsvolume/renamehandler/setvolumename(_:context:replyhandler:).md)
  Sets a new name for the volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolumerenameresult)*