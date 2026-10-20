# resume()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Resumes execution of a suspended task.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func resume() -> Bool
```

```objc
- (BOOL) resume;
```

#### Return Value

[`true`](../../Swift/true.md) if the receiver was able to resume execution, [`false`](../../Swift/false.md) otherwise.

#### Discussion

If the system sent multiple [`suspend()`](./suspend%28%29.md) messages to the receiver, an equal number of [`resume()`](./resume%28%29.md) messages must be sent before the task resumes execution.

## See Also

### Running and stopping
- [func run() throws](./run%28%29.md)
  Runs the process with the current environment.
- [func interrupt()](./interrupt%28%29.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func suspend() -> Bool](./suspend%28%29.md)
  Suspends execution of the receiver task.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/resume())*