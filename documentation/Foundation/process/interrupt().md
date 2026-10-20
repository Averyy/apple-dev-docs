# interrupt()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Sends an interrupt signal to the receiver and all of its subtasks.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
func interrupt()
```

```objc
- (void) interrupt;
```

#### Discussion

If the task terminates as a result, which is the default behavior, an [`didTerminateNotification`](./didterminatenotification.md) gets sent to the default notification center. This method has no effect if the receiver was already launched and has already finished executing. If the system hasn’t launched the receiver, this method raises an `NSInvalidArgumentException`.

It isn’t always possible to interrupt the receiver because it might be ignoring the interrupt signal. The [`interrupt()`](./interrupt%28%29.md) method sends `SIGINT`.

## See Also

### Running and stopping
- [func run() throws](./run%28%29.md)
  Runs the process with the current environment.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](./suspend%28%29.md)
  Suspends execution of the receiver task.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/interrupt())*