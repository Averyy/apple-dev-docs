# setVolumeName(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sets a new name for the volume.

**Availability**:
- macOS 15.4+ - Deprecated in 27.0

## Declaration

```swift
func setVolumeName(_ name: FSFileName, replyHandler reply: @escaping @Sendable (FSFileName?, (any Error)?) -> Void)
```

```swift
func setVolumeName(_ name: FSFileName) async throws -> FSFileName
```

```objc
- (void) setVolumeName:(FSFileName *) name replyHandler:(void (^)(FSFileName *newName, NSError *error)) reply;
```

## Parameters

- `name`: The new volume name.
- `reply`: A block or closure to indicate success or failure. If renaming succeeds, pass an [`FSFileName`](../../fsfilename.md) of the new volume name and a `nil` error. If renaming fails, pass the relevant error as the second parameter; FSKit ignores any [`FSFileName`](../../fsfilename.md) in this case. For an `async` Swift implementation, there’s no reply handler; simply return the [`FSFileName`](../../fsfilename.md) or throw an error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/renameoperations/setvolumename(_:replyhandler:))*