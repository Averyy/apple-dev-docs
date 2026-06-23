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

Use this type in your implementation of [`activate(options:replyHandler:)`](fsvolume/handler/activate(options:replyhandler:).md).

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
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func activate(options: FSTaskOptions, replyHandler: (FSActivateResult?, (any Error)?) -> Void)](fsvolume/handler/activate(options:replyhandler:).md)
  Activates the volume using the specified options.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsactivateresult)*