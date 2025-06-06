# terminate()

**Framework**: Foundation  
**Kind**: method

Sends a terminate signal to the receiver and all of its subtasks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func terminate()
```

#### Discussion

If the task terminates as a result, which is the default behavior, an [`didTerminateNotification`](process/didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the receiver hasn’t been launched yet, this method raises an `NSInvalidArgumentException`.

It’s not always possible to terminate the receiver because it might be ignoring the terminate signal. The [`terminate()`](process/terminate().md) method sends `SIGTERM`.

## See Also

- [func launch()](process/launch.md)
  Launches the task represented by the receiver.
- [class func launchedProcess(launchPath: String, arguments: [String]) -> Process](process/launchedprocess(launchpath:arguments:).md)
  Creates and launches a task with a specified executable and arguments.
- [var terminationStatus: Int32](process/terminationstatus.md)
  The exit status the receiver’s executable returns.
- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func interrupt()](process/interrupt.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](process/resume.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](process/suspend.md)
  Suspends execution of the receiver task.
- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminate())*