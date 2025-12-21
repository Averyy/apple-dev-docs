# wipe(_:completionHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Wipes existing file systems on the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func wipe(_ resource: FSBlockDeviceResource) async throws
```

#### Discussion

This method wraps the `wipefs` functionality from `libutil`. For more information, see the `man` page for `wipefs`.

## Parameters

- `resource`: The   to wipe.
- `completion`: A block or closure that executes after the wipe operation completes. The completion handler receives a single parameter indicating any error that occurs during the operation. If the value is  , the wipe operation succeeded.

## See Also

- [var containerStatus: FSContainerStatus](fsfilesystembase/containerstatus.md)
  The status of the file system container, indicating its readiness and activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystembase/wipe(_:completionhandler:))*