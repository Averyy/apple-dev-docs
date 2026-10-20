# run()

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

Runs the process with the current environment.

**Availability**:
- macOS 10.13+

## Declaration

```swift
func run() throws
```

```objc
- (BOOL) launchAndReturnError:(NSError **) error;
```

## See Also

### Running and stopping
- [func interrupt()](./interrupt%28%29.md)
  Sends an interrupt signal to the receiver and all of its subtasks.
- [func resume() -> Bool](./resume%28%29.md)
  Resumes execution of a suspended task.
- [func suspend() -> Bool](./suspend%28%29.md)
  Suspends execution of the receiver task.
- [func terminate()](./terminate%28%29.md)
  Sends a terminate signal to the receiver and all of its subtasks.
- [func waitUntilExit()](./waituntilexit%28%29.md)
  Blocks the process until the receiver is finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/process/run())*