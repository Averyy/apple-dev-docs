# terminationHandler

**Framework**: Foundation  
**Kind**: property

A completion block the system invokes when the task completes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var terminationHandler: ((Process) -> Void)? { get set }
```

#### Discussion

The system passes the task object to the block to allow access to the task parameters, for example to determine if the task completed successfully.

This block isn’t guaranteed to be fully executed prior to [`waitUntilExit()`](process/waituntilexit().md) returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationhandler)*