# isRunning

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A status that indicates whether the receiver is still running.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.0+

## Declaration

```swift
var isRunning: Bool { get }
```

```objc
@property (readonly, getter=isRunning) BOOL running;
```

## Return Value

[`true`](../../Swift/true.md) if the receiver is still running, otherwise [`false`](../../Swift/false.md). [`false`](../../Swift/false.md) means either the receiver could not run or it has terminated.

## See Also

### Related Documentation
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.
- [func launch()](./launch%28%29.md)
  Launches the task represented by the receiver.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
### Querying the process state
- [var terminationStatus: Int32](./terminationstatus.md)
  The exit status the receiver’s executable returns.
- [var terminationReason: Process.TerminationReason](./terminationreason-swift.property.md)
  The reason the system terminated the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/isrunning)*