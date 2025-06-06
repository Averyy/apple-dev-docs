# suspend()

**Framework**: Foundation  
**Kind**: method

Suspends execution of the receiver task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func suspend() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver was successfully suspended, [`false`](https://developer.apple.com/documentation/swift/false) otherwise.

#### Discussion

Multiple [`suspend()`](process/suspend().md) messages can be sent, but they must be balanced with an equal number of [`resume()`](process/resume().md) messages before the task resumes execution.

## See Also

- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func interrupt()](process/interrupt.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](process/resume.md)
  Resumes execution of a suspended task.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/suspend())*