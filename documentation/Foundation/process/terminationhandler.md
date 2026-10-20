# terminationHandler

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

A completion block the system invokes when the task completes.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var terminationHandler: (@Sendable (Process) -> Void)? { get set }
```

```objc
@property (copy, nullable) void (^)(NSTask *) terminationHandler;
```

#### Discussion

The system passes the task object to the block to allow access to the task parameters, for example to determine if the task completed successfully.

This block isn’t guaranteed to be fully executed prior to [`waitUntilExit()`](./waituntilexit%28%29.md) returning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/terminationhandler)*