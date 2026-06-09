# deactivateItem(_:context:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Notifies the file system that the kernel is no longer making immediate use of the given item.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func deactivateItem(_ item: FSItem, context: FSContext) async throws -> FSDeactivateItemResult
```

#### Discussion

This method gives a file system a chance to release resources associated with an item. However, this method prescribes no specific action; it’s acceptable to defer all reclamation until [`reclaimItem(_:replyHandler:)`](fsvolume/handler/reclaimitem(_:replyhandler:).md). This method is the equivalent of VFS’s `VNOP_INACTIVE`.

FSKit restricts calls to this method based on the current value of [`itemDeactivationPolicy`](fsvolume/itemdeactivation/itemdeactivationpolicy.md).

## Parameters

- `item`: The item to deactivate.
- `context`: An object that enables context-aware file system decisions throughout the operation.
- `reply`: A block or closure to indicate success or failure. If deactivation succeeds, pass an instance of [`FSDeactivateItemResult`](fsdeactivateitemresult.md) containing the volume’s updated free space, along with a `nil` error. If deactivation fails, pass the relevant error as the second parameter; FSKit ignores the [`FSDeactivateItemResult`](fsdeactivateitemresult.md) instance in this case. For an `async` Swift implementation, there’s no reply handler; simply return the result instance or throw an error.

## See Also

- [class FSDeactivateItemResult](fsdeactivateitemresult.md)
  The result of a deactivate-item call.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivationhandler/deactivateitem(_:context:replyhandler:))*