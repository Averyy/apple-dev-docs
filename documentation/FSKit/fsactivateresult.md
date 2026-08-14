# FSActivateResult

**Framework**: FSKit  
**Kind**: class

The result of an activate call.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSActivateResult
```

#### Overview

Use this type in your implementation of [`activateVolume(options:replyHandler:)`](fsvolume/handler/activatevolume(options:replyhandler:).md).

## Topics

### Creating an activate result
- [init?(rootItem: FSItem)](fsactivateresult/init(rootitem:).md)
  Creates an activate result instance.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.

## Relationships

### Inherits From
- [FSVolumeHandlerResult](fsvolumehandlerresult.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsactivateresult)*