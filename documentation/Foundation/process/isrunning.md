# isRunning

**Framework**: Foundation  
**Kind**: property

A status that indicates whether the receiver is still running.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var isRunning: Bool { get }
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the receiver is still running, otherwise [`false`](https://developer.apple.com/documentation/swift/false). [`false`](https://developer.apple.com/documentation/swift/false) means either the receiver could not run or it has terminated.

## See Also

- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.
- [func launch()](process/launch.md)
  Launches the task represented by the receiver.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [var terminationStatus: Int32](process/terminationstatus.md)
  The exit status the receiver’s executable returns.
- [var terminationReason: Process.TerminationReason](process/terminationreason-swift.property.md)
  The reason the system terminated the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/isrunning)*