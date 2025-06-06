# unmount(replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Unmounts this volume.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func unmount() async
```

#### Discussion

Clear and flush all cached state in your implementation of this method.

## Parameters

- `reply`: A block or closure to indicate success or failure. If unmounting fails, pass an error as the one parameter to the reply handler. If unmounting succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply return normally.

## See Also

- [func mount(options: FSTaskOptions, replyHandler: ((any Error)?) -> Void)](fsvolume/operations/mount(options:replyhandler:).md)
  Mounts this volume, using the specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/unmount(replyhandler:))*