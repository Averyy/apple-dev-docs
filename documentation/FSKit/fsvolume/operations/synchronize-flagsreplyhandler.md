# synchronize(flags:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Synchronizes the volume with its underlying resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func synchronize(flags: FSSyncFlags) async throws
```

#### Discussion

After calling this method, FSKit assumes that the volume has sent all pending I/O or metadata to its resource.

## Parameters

- `flags`: Timing flags, as defined in `mount.h.` These flags let the file system know whether to run the operation in a blocking or nonblocking fashion.
- `reply`: A block or closure to indicate success or failure. If synchronization fails, pass an error as the one parameter to the reply handler. If synchronization succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/operations/synchronize(flags:replyhandler:))*