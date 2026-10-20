# wipe(_:completionHandler:)

**Framework**: FSKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Wipes existing file systems on the specified resource.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func wipe(_ resource: FSBlockDeviceResource, completionHandler completion: @escaping @Sendable ((any Error)?) -> Void)
```

```swift
func wipe(_ resource: FSBlockDeviceResource) async throws
```

```objc
- (void) wipeResource:(FSBlockDeviceResource *) resource completionHandler:(void (^)(NSError *error)) completion;
```

#### Discussion

This method wraps the `wipefs` functionality from `libutil`. For more information, see the `man` page for `wipefs`.

## Parameters

- `resource`: The [`FSBlockDeviceResource`](../fsblockdeviceresource.md) to wipe.
- `completion`: A block or closure that executes after the wipe operation completes. The completion handler receives a single parameter indicating any error that occurs during the operation. If the value is `nil`, the wipe operation succeeded.

## See Also

### Implementing essential functionality
- [var containerStatus: FSContainerStatus](./containerstatus.md)
  The status of the file system container, indicating its readiness and activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsfilesystembase/wipe(_:completionhandler:))*