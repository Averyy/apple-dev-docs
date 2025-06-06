# activate(options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Activates the volume using the specified options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func activate(options: FSTaskOptions) async throws -> FSItem
```

#### Discussion

When FSKit calls this method, allocate any in-memory state required to represent the file system. Also allocate an [`FSItem`](fsitem.md) for the root directory of the file system, and pass it to the reply block. FSKit caches this root item for the lifetime of the volume, and uses it as a starting point for all file look-ups.

Volume activation occurs prior to any call to mount the volume.

## Parameters

- `options`: Options to apply to the activation. These can include security-scoped file paths. There are no defined options currently.
- `reply`: A block or closure to indicate success or failure. If activation succeeds, pass the root   and a   error. If activation fails, pass the relevant error as the second parameter; FSKit ignores any   in this case. In Swift,   takes only the   as the parameter; you signal any error with a  . For an   Swift implementation, there’s no reply handler; simply return the   or throw an error.

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/activate(options:replyhandler:))*