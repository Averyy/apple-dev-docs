# cancellationHandler

**Framework**: FSKit  
**Kind**: property

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
var cancellationHandler: (() -> (any Error)?)? { get set }
```

#### Return Value

An error if the cancellation did not complete successfully. Any returned error will be logged, and FSKit will then terminate all activity in the container.

#### Discussion

```obj-c
{
NSProgress *progress = [[NSProgress alloc] init];
yourFileSystemChecker *checker= [[yourFileSystemChecker alloc] init];
checker.work_group = dispatch_group_create();
dispatch_group_enter(checker.work_group);
[task setCancellationHandler:^NSError * _Nullable{
    checker.terminate = TRUE;
    dispatch_group_wait(checker.work_group);
    return nil;
}];
dispatch_async(someQueue, ^{[self performCheck:task progress:progress];});
return progress;
}
```

> **Note**: This example did not account for errors while delivered code must. finally, the `performCheck` code should perform the check operation. It should periodically update the progress object and check its `interrupted` variable. The check can either complete successfully, complete with an error, or be interrupted. It should then call `[task didCompleteWithError:...]` wtih the appropriate error value or nil. Finally it should `dispatch_group_leave(self.work_group);`


---

*[View on Apple Developer](https://developer.apple.com/documentation/fskit/fstask/cancellationhandler)*