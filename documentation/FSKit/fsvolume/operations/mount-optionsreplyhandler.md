# mount(options:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Mounts this volume, using the specified options.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func mount(options: FSTaskOptions) async throws
```

#### Discussion

FSKit calls this method as a signal that some process is trying to mount this volume. Your file system receives a call to [`activate(options:replyHandler:)`](fsvolume/operations/activate(options:replyhandler:).md) prior to receiving any mount calls.

## Parameters

- `options`: Options to apply to the mount. These can include security-scoped file paths. There are no defined options currently.
- `reply`: A block or closure to indicate success or failure. If mounting fails, pass an error as the one parameter to the reply handler. If mounting succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply return normally.

## See Also

- [func unmount(replyHandler: () -> Void)](fsvolume/operations/unmount(replyhandler:).md)
  Unmounts this volume.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/mount(options:replyhandler:))*