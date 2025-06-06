# finishRunningWithError(_:)

**Framework**: Automator  
**Kind**: method

Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
func finishRunningWithError(_ error: (any Error)?)
```

#### Discussion

Call this method on any action that overrides [`runAsynchronously(withInput:)`](amaction/runasynchronously(withinput:).md) in order to make asynchronous calls. When [`finishRunningWithError(_:)`](amaction/finishrunningwitherror(_:).md) is invoked, it immediately calls [`willFinishRunning()`](amaction/willfinishrunning().md).

## Parameters

- `error`: The error to be returned to Automator.

## See Also

- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](amaction/stop.md)
  Stops the action from running.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/finishrunningwitherror(_:))*