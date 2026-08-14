# cancellationHandler

**Framework**: FSKit  
**Kind**: property

A handler called by FSKit upon canceling the task.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var cancellationHandler: (@Sendable () -> (any Error)?)? { get set }
```

#### Discussion

FSKit calls the cancellation handler within an independent execution context.

If the handler can’t complete its work successfully, it can return an error from the block or closure. FSKit logs any returned error and then terminates all activity in the container.

The task object clears its `cancellationHandler` property after the task’s cancellation or completion. This helps accelerate the cleanup of retained state.

The exact structuring of the completion handler depends on the structuring of the code implementing the task. As a concrete example, consider a check operation with the following class:

**Objective-C**:

```obj-c
@‎‌interface YourFileSystem : NSObject
@property (retain) dispatch_group_t work_group;
@property (nonatomic,getter=interrupted) BOOL interrupted;
@end
```

**Swift**:

```swift
class YourFileSystem {
    let work_group: dispatch_group_t = DispatchGroup()
    var interrupted: Bool = false
    private lazy var leaveWorkGroupOnce = leaveWorkGroup()
}
```

and a `startCheckWithTask` method with a helper method `performCheck` like the following:

**Objective-C**:

```obj-c
- (void)performCheck:(nonnull FSTask *)task
            progress:(nonnull NSProgress *)progress
             context:(YourFileSystemCancelationContext *)context {
             // See discussion for notes on implementing this method.
  }

- (NSProgress * _Nullable)startCheckWithTask:(nonnull FSTask *)task
                                     options:(nonnull FSTaskOptions *)options
                                       error:(NSError *__autoreleasing  _Nullable * _Nullable)error {
    dispatch_queue_t someQueue = dispatch_get_global_queue(DISPATCH_QUEUE_PRIORITY_DEFAULT, 0);
    NSProgress *progress = [[NSProgress alloc] init];
    YourFileSystemCancelationContext *checker= [[YourFileSystemCancelationContext alloc] init];
    dispatch_group_enter(checker.work_group);
    [task setCancellationHandler:^NSError * _Nullable{
        checker.interrupted = YES;
        dispatch_group_wait(checker.work_group, DISPATCH_TIME_FOREVER);
        return nil;
    }];
    dispatch_async(someQueue, ^{[self performCheck:task progress:progress context:checker];});
    return progress;
}
```

**Swift**:

```swift
func performCheck(task: FSTask, progress: Progress,
                  context: YourFileSystemCancelationContext) {
   // See discussion for notes on implementing this method.
}

func startCheck(task: FSTask, options: FSTaskOptions) throws -> Progress {
    let someQueue = DispatchQueue.global()
    let progress = Progress()
    let checkContext = YourFileSystemCancelationContext()
    checkContext.work_group.enter()
    task.cancellationHandler = {
        checkContext.interrupted = true
        checkContext.work_group.wait()
        return nil
    }
    someQueue.async {
        self.performCheck(task: task, progress: progress, context:checkContext)
    }
    return progress
}
```

When canceled, the handler block in this example sets the checker’s `interrupted` property, and then calls the [`DispatchGroup`](https://developer.apple.com/documentation/dispatch/dispatchgroup) method [`wait()`](https://developer.apple.com/documentation/dispatch/dispatchgroup/wait()) (Swift) or the function [`dispatch_group_wait`](https://developer.apple.com/documentation/dispatch/dispatch_group_wait) (Objective-C) on the checker’s work group. Because neither of these operations can fail, the handler returns `nil` to indicate it didn’t encounter an error.

For simplicity, this example doesn’t account for errors, whereas production code must do so. Furthermore, when fully implemented, the `performCheck` method should perform a check operation. Specifically, it should periodically update the progress object and check its `interrupted` variable. The check can either complete successfully, complete with an error, or enter the interrupted state. It should then call [`didComplete(error:)`](fstask/didcomplete(error:).md) with the appropriate error value or `nil`. Finally it should call `context.work_group.leave()` (Swift) or `dispatch_group_leave(context.work_group)` (Objective-C) to remove itself from its dispatch group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask/cancellationhandler)*