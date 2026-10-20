# suspend()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Suspends execution of the receiver task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func suspend() -> Bool
```

```objc
- (BOOL) suspend;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver was successfully suspended, [`false`](../../Swift/false.md) otherwise.

#### Discussion

Multiple [`suspend()`](./suspend%28%29.md) messages can be sent, but they must be balanced with an equal number of [`resume()`](./resume%28%29.md) messages before the task resumes execution.

## See Also

### Running and stopping
- [func run() throws](./run%28%29.md)
  Runs the process with the current environment.
- [func interrupt()](./interrupt%28%29.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes execution of a suspended task.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/suspend())*