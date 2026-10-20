# stop()

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Stops the action from running.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.4+

## Declaration

```swift
func stop()
```

```objc
- (void) stop;
```

#### Discussion

The output acquired by the action during execution of the current workflow is still accessible to Automator.

## See Also

### Controlling the Action
- [func run(withInput: Any?) throws -> Any](./run%28withinput%29.md)
  Requests the action to perform its task using the specified input.
- [func runAsynchronously(withInput: Any?)](./runasynchronously%28withinput%29.md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](./finishrunningwitherror%28_%29.md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](./willfinishrunning%28%29.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func reset()](./reset%28%29.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/stop())*