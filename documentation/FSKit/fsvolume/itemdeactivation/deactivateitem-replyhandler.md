# deactivateItem(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Notifies the file system that the kernel is no longer making immediate use of the given item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func deactivateItem(_ item: FSItem) async throws
```

#### Discussion

This method gives a file system a chance to release resources associated wtih an item. However, this method prescribes no specific action; it’s acceptable to defer all reclamation until [`reclaimItem(_:replyHandler:)`](fsvolume/operations/reclaimitem(_:replyhandler:).md). This method is the equivalent of VFS’s `VNOP_INACTIVE`.

FSKit restricts calls to this method based on the current value of [`itemDeactivationPolicy`](fsvolume/itemdeactivation/itemdeactivationpolicy.md).

## Parameters

- `item`: The item to deactivate.
- `reply`: A block or closure to indicate success or failure. If deactivation fails, pass an error as the one parameter to the reply handler. If deactivation succeeds, pass  . For an   Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/itemdeactivation/deactivateitem(_:replyhandler:))*