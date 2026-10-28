# FSActivateResult

**Framework**: FSKit  
**Kind**: class  
**Role**: Class

The result of an activate call.

**Availability**:
- macOS 27.0+

## Declaration

```swift
class FSActivateResult
```

```objc
@interface FSActivateResult : FSVolumeHandlerResult
```

## Overview

Use this type in your implementation of [`activateVolume(options:replyHandler:)`](./fsvolume/handler/activatevolume%28options,replyhandler%29.md).

## Topics

### Creating an activate result
- [init?(rootItem: FSItem)](./fsactivateresult/init%28rootitem%29.md)
  Creates an activate result instance.
- [class FSItem](./fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.

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

### Handling activation and deactivation
- [class FSItem](./fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [struct FSDeactivateOptions](./fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsactivateresult)*