# deactivate(options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Tears down a previously initialized volume instance.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func deactivate(options: FSDeactivateOptions = []) async throws
```

#### Discussion

Set up your implementation to release any resources allocated for the volume instance. By the time you receive this callback, FSKit has already performed a reclaim call to release all other file nodes associated with this file system instance.

Avoid performing any I/O in this method. Prior to calling this method, FSKit has already issued a sync call to perform any cleanup-related I/O.

FSKit unmounts any mounted volume with a call to [`unmount(replyHandler:)`](fsvolume/operations/unmount(replyhandler:).md) prior to the deactivate callback.

## Parameters

- `options`: Options to apply to the deactivation.
- `reply`: A block or closure to indicate success or failure. If activation fails, pass an error as the one parameter to the reply handler. If activation succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.

## See Also

- [func activate(options: FSTaskOptions, replyHandler: (FSItem?, (any Error)?) -> Void)](fsvolume/operations/activate(options:replyhandler:).md)
  Activates the volume using the specified options.
- [class FSItem](fsitem.md)
  A distinct object in a file hierarchy, such as a file, directory, symlink, socket, and more.
- [struct FSDeactivateOptions](fsdeactivateoptions.md)
  Options that affect the behavior of deactivate methods.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/deactivate(options:replyhandler:))*