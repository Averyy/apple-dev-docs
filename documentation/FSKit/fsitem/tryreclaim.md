# tryReclaim(_:)

**Framework**: FSKit  
**Kind**: method

Reclaims the item by executing the given block, if conditions allow.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
func tryReclaim(_ reclaimBlock: @escaping () -> Void) -> Bool
```

#### Return Value

`true` (Swift) or YES (Obj-C)  if the reclaim block ran; otherwise, `false` (Swift) or `NO` (Obj-C). When your [`reclaimItem(_:replyHandler:)`](fsvolume/handler/reclaimitem(_:replyhandler:).md) implementation receives a `false`/`NO` return value, call `replyHandler(nil)`.

#### Discussion

Invoke this method in your implementation of the [`reclaimItem(_:replyHandler:)`](fsvolume/handler/reclaimitem(_:replyhandler:).md) operation.

FSKit internally maintains a count of how many times it returns each [`FSItem`](fsitem.md) to the kernel, via either a creation operation or a lookup. The kernel file system also maintains a count of how many times a create or a lookup operation returned a vnode. When the kernel reclaims the vnode associated with an FSItem, the FSItem is only eligible for reclaiming when both the kernel and user space counts agree. This mechanism addresses a potential race condition in which concurrent reclaim and lookup operations might lead to a lookup returning a deallocated [`FSItem`](fsitem.md), and as a result, induce undefined behavior. File systems that don’t invoke this method during reclaim are exposed to this race condition.

> ❗ **Important**: The caller must invoke this method within a synchronization context that ensures the [`FSItem`](fsitem.md) isn’t concurrently returned by lookup operations.

Example Usage:

**Swift**:

```swift
func reclaimItem(_ item: FSItem,
                 replyHandler reply: @escaping @Sendable ((any Error)?) -> Void) {
    var reclaimError: NSError? = nil // To be set during the reclaim block in case of an error.

    // *** CRITICAL SECTION BEGINS HERE ***
    // (A synchronization context that ensures the FSItem isn't concurrently returned by lookup operations)

    // Calling `tryReclaim(_:)` with the cleanup logic within the passed block
    let wasReclaimed = item.tryReclaim( {
        // Closure includes all required cleanup operations for reclaiming this item.
        // Sets `reclaimError` in case of an error during the cleanup phase.
    } )

    // *** CRITICAL SECTION ENDS HERE ***

    if (wasReclaimed) {
        // Clean up the FSItem if special teardown is needed.
        reply(reclaimError)
    } else {
        // Do nothing; the FSItem wasn't reclaimed, so it's not yet time to run cleanup.
        reply(nil)
    }
}
```

**Objective-C**:

```objc
- (void)reclaimItem:(FSItem *)item
    replyHandler:(void(^)(NSError * _Nullable error))reply
{
    __block NSError *reclaimError = nil; // To be set during the reclaim block in case of an error.

    // *** CRITICAL SECTION BEGINS HERE ***
    // (A synchronization context that ensures the FSItem isn't concurrently returned by lookup operations)

    // Calling `tryReclaimWithBlock:` with the cleanup logic within the passed block
    BOOL wasReclaimed = [item tryReclaimWithBlock:^{
        // Includes all required cleanup operations for reclaiming this item.
        // Sets `reclaimError` in case of an error during the cleanup phase
    }];

    // *** CRITICAL SECTION ENDS HERE ***

    if (wasReclaimed) {
        // Clean up the FSItem if special teardown is needed.
        reply(reclaimError);
    } else {
        // Do nothing; the FSItem wasn't reclaimed, so it's not yet time to run cleanup.
        reply(nil);
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fsitem/tryreclaim(_:))*