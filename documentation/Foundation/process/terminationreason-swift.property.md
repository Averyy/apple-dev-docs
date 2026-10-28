# terminationReason

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The reason the system terminated the task.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var terminationReason: Process.TerminationReason { get }
```

```objc
@property (readonly) NSTaskTerminationReason terminationReason;
```

## Return Value

The termination status. The possible values are described in [`Process.TerminationReason`](./terminationreason-swift.enum.md).

## See Also

### Querying the process state
- [var isRunning: Bool](./isrunning.md)
  A status that indicates whether the receiver is still running.
- [var terminationStatus: Int32](./terminationstatus.md)
  The exit status the receiver’s executable returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationreason-swift.property)*