# stop()

**Framework**: Automator  
**Kind**: method

Stops the action from running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func stop()
```

#### Discussion

The output acquired by the action during execution of the current workflow is still accessible to Automator.

## See Also

- [func run(withInput: Any?) throws -> Any](amaction/run(withinput:).md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/stop())*