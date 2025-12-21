# cancellationHandler

**Framework**: FSKit  
**Kind**: property

A handler called by FSKit upon canceling the task.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var cancellationHandler: (() -> (any Error)?)? { get set }
```

#### Discussion

FSKit calls the cancellation handler within an independent execution context.

If the handler can’t complete its work successfully, it can return an error from the block or closure. FSKit logs any returned error and then terminates all activity in the container.

The task object clears its `cancellationHandler` property after the task’s cancellation or completion. This helps accelerate the cleanup of retained state.

The exact structuring of the completion handler depends on the structuring of the code imlementing the task. As a concrete example, consider a check operation with the following class:

and a `startCheckWithTask` method with a helper method `performCheck` like the following:

When canceled, the handler block in this example sets the checker’s `interrupted` property, and then calls the [`DispatchGroup`](https://developer.apple.com/documentation/Dispatch/DispatchGroup) method [`wait()`](https://developer.apple.com/documentation/Dispatch/DispatchGroup/wait()) (Swift) or the function [`dispatch_group_wait`](https://developer.apple.com/documentation/Dispatch/dispatch_group_wait) (Objective-C) on the checker’s work group. Because neither of these operations can fail, the handler returns `nil` to indicate it didn’t encounter an error.

For simplicity, this example doesn’t account for errors, whereas production code must do so. Furthermore, when fully implemented, the `performCheck` method should perform a check operation. Specifically, it should periodically update the progress object and check its `interrupted` variable. The check can either complete successfully, complete with an error, or enter the interrupted state. It should then call [`didComplete(error:)`](fstask/didcomplete(error:).md) wtih the appropriate error value or `nil`. Finally it should call `context.work_group.leave()` (Swift) or `dispatch_group_leave(context.work_group)` (Objective-C) to remove itself from its dispatch group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask/cancellationhandler)*