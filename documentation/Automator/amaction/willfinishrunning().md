# willFinishRunning()

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
func willFinishRunning()
```

```objc
- (void) willFinishRunning;
```

#### Discussion

Overridde this method in actions that need to make asynchronous calls. Automator invokes this method when the action is about to complete its run phase.

## See Also

### Controlling the Action
- [func run(withInput: Any?) throws -> Any](./run%28withinput%29.md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](./runasynchronously%28withinput%29.md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](./finishrunningwitherror%28_%29.md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func stop()](./stop%28%29.md)
  Stops the action from running.
- [func reset()](./reset%28%29.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/willfinishrunning())*