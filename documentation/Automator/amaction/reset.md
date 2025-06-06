# reset()

**Framework**: Automator  
**Kind**: method

Resets the action to its initial state.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func reset()
```

#### Discussion

Resetting causes the action to release its output generated from the current execution of the workflow.

## See Also

- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](amaction/stop.md)
  Stops the action from running.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/reset())*