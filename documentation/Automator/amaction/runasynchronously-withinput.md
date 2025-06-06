# runAsynchronously(withInput:)

**Framework**: Automator  
**Kind**: method

Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
func runAsynchronously(withInput input: Any?)
```

#### Discussion

Override this method in actions that need to make asynchronous calls. After [`runAsynchronously(withInput:)`](amaction/runasynchronously(withinput:).md) is invoked, Automator doesn’t continue until the action invokes [`finishRunningWithError(_:)`](amaction/finishrunningwitherror(_:).md). In your override of this method, you can make an asynchronous call, wait to be notified of its completion, then invoke [`finishRunningWithError(_:)`](amaction/finishrunningwitherror(_:).md) to signal to Automator that the action has completed.

> ⚠️ **Warning**:  Failure to invoke [`finishRunningWithError(_:)`](amaction/finishrunningwitherror(_:).md) can cause a workflow to stall indefinitely.

 Failure to invoke [`finishRunningWithError(_:)`](amaction/finishrunningwitherror(_:).md) can cause a workflow to stall indefinitely.

For actions that don’t need to make asynchronous calls, use [`runWithInput:fromAction:error:`](amaction/runwithinput:fromaction:error:.md) instead.

## Parameters

- `input`: The input for the action. Should contain one or more objects compatible with one of the types specified in the action’s   property.

## See Also

- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](amaction/stop.md)
  Stops the action from running.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/runasynchronously(withinput:))*