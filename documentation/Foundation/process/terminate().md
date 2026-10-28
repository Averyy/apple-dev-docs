# terminate()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends a terminate signal to the receiver and all of its subtasks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func terminate()
```

```objc
- (void) terminate;
```

## Discussion

If the task terminates as a result, which is the default behavior, an [`didTerminateNotification`](./didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the receiver hasn’t been launched yet, this method raises an `NSInvalidArgumentException`.

It’s not always possible to terminate the receiver because it might be ignoring the terminate signal. The [`terminate()`](./terminate%28%29.md) method sends `SIGTERM`.

## See Also

### Related Documentation
- [func launch()](./launch%28%29.md)
  Launches the task represented by the receiver.
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](./launchedprocess%28launchpath,arguments%29.md)
  Creates and launches a task with a specified executable and arguments.
- [var terminationStatus: Int32](./terminationstatus.md)
  The exit status the receiver’s executable returns.
### Running and stopping
- [func run() throws](./run%28%29.md)
  Runs the process with the current environment.
- [func interrupt()](./interrupt%28%29.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](./suspend%28%29.md)
  Suspends execution of the receiver task.
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminate())*