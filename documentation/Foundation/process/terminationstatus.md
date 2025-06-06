# terminationStatus

**Framework**: Foundation  
**Kind**: property

The exit status the receiver’s executable returns.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var terminationStatus: Int32 { get }
```

#### Return Value

The exit status returned by the receiver’s executable.

#### Discussion

Each task defines and documents how your app should interpret the return value. For example, many commands return 0 if they complete successfully or an error code if they don’t. You’ll need to look at the documentation for that task to learn what values it returns under what circumstances.

This method raises an `NSInvalidArgumentException` if the receiver is still running. Verify that the receiver isn’t running before you use it.

## See Also

- [func waitUntilExit()](process/waituntilexit.md)
  Blocks the process until the receiver is finished.
- [func terminate()](process/terminate.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [var isRunning: Bool](process/isrunning.md)
  A status that indicates whether the receiver is still running.
- [var terminationReason: Process.TerminationReason](process/terminationreason-swift.property.md)
  The reason the system terminated the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationstatus)*