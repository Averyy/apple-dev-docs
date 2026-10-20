# runAsynchronously(withInput:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.5+

## Declaration

```swift
func runAsynchronously(withInput input: Any?)
```

```objc
- (void) runAsynchronouslyWithInput:(id) input;
```

#### Discussion

Override this method in actions that need to make asynchronous calls. After [`runAsynchronously(withInput:)`](./runasynchronously%28withinput%29.md) is invoked, Automator doesn’t continue until the action invokes [`finishRunningWithError(_:)`](./finishrunningwitherror%28_%29.md). In your override of this method, you can make an asynchronous call, wait to be notified of its completion, then invoke [`finishRunningWithError(_:)`](./finishrunningwitherror%28_%29.md) to signal to Automator that the action has completed.

> ⚠️ **Warning**:  Failure to invoke [`finishRunningWithError(_:)`](./finishrunningwitherror%28_%29.md) can cause a workflow to stall indefinitely.

For actions that don’t need to make asynchronous calls, use [`runWithInput:fromAction:error:`](./runwithinput_fromaction_error_.md) instead.

## Parameters

- `input`: The input for the action. Should contain one or more objects compatible with one of the types specified in the action’s [`selectedInputType`](./selectedinputtype.md) property.

## See Also

### Controlling the Action
- [func run(withInput: Any?) throws -> Any](./run%28withinput%29.md)
  Requests the action to perform its task using the specified input.
- [func finishRunningWithError((any Error)?)](./finishrunningwitherror%28_%29.md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](./willfinishrunning%28%29.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](./stop%28%29.md)
  Stops the action from running.
- [func reset()](./reset%28%29.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/runasynchronously(withinput:))*