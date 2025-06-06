# willFinishRunning()

**Framework**: Automator  
**Kind**: method

Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
func willFinishRunning()
```

#### Discussion

Overridde this method in actions that need to make asynchronous calls. Automator invokes this method when the action is about to complete its run phase.

## See Also

- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func stop()](amaction/stop.md)
  Stops the action from running.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/willfinishrunning())*