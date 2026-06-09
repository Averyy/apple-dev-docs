# FSActivateResult

**Framework**: FSKit  
**Kind**: class

Result class for [`activate(options:replyHandler:)`](fsvolume/handler/activate(options:replyhandler:).md)

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
class FSActivateResult
```

## Topics

### Creating an activate result
- [init?(rootItem: FSItem)](fsactivateresult/init(rootitem:).md)
  Creates a result instance with all required properties populated.
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