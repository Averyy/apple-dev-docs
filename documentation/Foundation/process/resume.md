# resume()

**Framework**: Foundation  
**Kind**: method

Resumes execution of a suspended task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resume() -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the receiver was able to resume execution, [`false`](https://developer.apple.com/documentation/Swift/false) otherwise.

#### Discussion

If the system sent multiple [`suspend()`](process/suspend().md) messages to the receiver, an equal number of [`resume()`](process/resume().md) messages must be sent before the task resumes execution.

## See Also

- [func run() throws](process/run.md)
  Runs the process with the current environment.
- [func interrupt()](process/interrupt.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func suspend() -> Bool](process/suspend.md)
  Suspends execution of the receiver task.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/resume())*