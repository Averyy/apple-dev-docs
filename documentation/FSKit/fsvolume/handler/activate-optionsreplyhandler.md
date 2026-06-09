# activate(options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Activates the volume using the specified options.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func activate(options: FSTaskOptions) async throws -> FSActivateResult
```

#### Discussion

When FSKit calls this method, allocate any in-memory state required to represent the file system. Also allocate an [`FSItem`](fsitem.md) for the root directory of the file system, and pass it to the reply block. FSKit caches this root item for the lifetime of the volume, and uses it as a starting point for all file look-ups.

Volume activation occurs prior to any call to mount the volume.

## Parameters

- `options`: Options to apply to the activation. These can include security-scoped file paths. There are no defined options currently.
- `reply`: A block or closure to indicate success or failure. If activation succeeds, pass an instance of [`FSActivateResult`](fsactivateresult.md) containing the root [`FSItem`](fsitem.md), along with a `nil` error. If activation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSActivateResult`](fsactivateresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [class FSActivateResult](fsactivateresult.md)
  Result class for [`activate(options:replyHandler:)`](fsvolume/handler/activate(options:replyhandler:).md)
- [func deactivate(options: FSDeactivateOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/handler/deactivate(options:replyhandler:).md)
  Tears down a previously initialized volume instance.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/handler/activate(options:replyhandler:))*