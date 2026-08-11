# reclaimItem(_:replyHandler:)

**Framework**: FSKit  
**Kind**: method  
**Required**: Yes

Reclaims an item, releasing any resources allocated for the item.

**Availability**:
- macOS 15.4+

## Declaration

```swift
func reclaimItem(_ item: FSItem) async throws
```

#### Discussion

FSKit guarantees that for every [`FSItem`](fsitem.md) returned by the volume, a corresponding reclaim operation occurs after the upper layers no longer reference that item. To use this behavior, call [`tryReclaim(_:)`](fsitem/tryreclaim(_:).md) in your implementation of this method.

> **Note**: Block device file systems may assess whether an underlying resource terminates before processing reclaim operations. On unary file systems, for example, the associated volumes unmount when such resources disconnect from the system. The unmount triggers a reclaiming of all items. Some implementations benefit greatly from short-circuiting in such cases. With a terminated resource, all I/O results in an error, making short-circuiting the most efficient response.

## Parameters

- `item`: The item to reclaim.
- `reply`: A block or closure to indicate success or failure. If removal fails, pass an error as the one parameter to the reply handler. If removal succeeds, pass `nil`. For an `async` Swift implementation, there’s no reply handler; simply throw an error or return normally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsvolume/commonoperations/reclaimitem(_:replyhandler:))*