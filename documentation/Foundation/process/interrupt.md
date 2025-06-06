# interrupt()

**Framework**: Foundation  
**Kind**: method

Sends an interrupt signal to the receiver and all of its subtasks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func interrupt()
```

#### Discussion

If the task terminates as a result, which is the default behavior, an [`didTerminateNotification`](process/didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the system hasn’t launched the receiver, this method raises an `NSInvalidArgumentException`.

It isn’t always possible to interrupt the receiver because it might be ignoring the interrupt signal. The [`interrupt()`](process/interrupt().md) method sends `SIGINT`.

## See Also

- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func resume() -> Bool](process/resume.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](process/suspend.md)
  Suspends execution of the receiver task.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/interrupt())*