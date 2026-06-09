# setVolumeName(_:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Sets a new name for the volume.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func setVolumeName(_ name: FSFileName, context: FSContext) async throws -> FSVolumeRenameResult
```

## Parameters

- `name`: The new volume name.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If renaming succeeds, pass an instance of [`FSVolumeRenameResult`](fsvolumerenameresult.md) containing the [`FSFileName`](fsfilename.md) of the new volume name, along with a `nil` error. If renaming fails, pass the relevant error as the second parameter; FSKit ignores the [`FSVolumeRenameResult`](fsvolumerenameresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSVolumeRenameResult](fsvolumerenameresult.md)
  The result of a rename-volume call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renamehandler/setvolumename(_:context:replyhandler:))*