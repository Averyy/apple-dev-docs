# dispatch_block_cancel

**Framework**: Dispatch  
**Kind**: func  
**Role**: Function

Cancels the specified dispatch block asynchronously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```c
extern void dispatch_block_cancel(dispatch_block_t block);
```

## Discussion

Cancellation causes any future execution of the dispatch block to return immediately, but does not affect any execution of the block object that is already in progress.

Release of any resources associated with the block object is delayed until execution of the block object is next attempted (or any execution already in progress completes).

> **Note**:  Take care to ensure that a block object that may be canceled does not capture any resources that require execution of the block body in order to be released, such as memory allocated with `malloc(3)` on which the block body calls `free(3)`. Such resources are leaked if the block body is never executed due to cancellation.

## Parameters

- `block`: The dispatch block to cancel.

  The result of passing `NULL` or a block object not returned by the [`dispatch_block_create`](./dispatch_block_create.md) or [`dispatch_block_create_with_qos_class`](./dispatch_block_create_with_qos_class.md) function is undefined.

## See Also

### Canceling a Work Item
- [dispatch_block_testcancel](./dispatch_block_testcancel.md)
  Tests whether the given dispatch block has been canceled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/dispatch/dispatch_block_cancel)*