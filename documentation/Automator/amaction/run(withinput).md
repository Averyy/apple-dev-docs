# run(withInput:)

**Framework**: Automator  
**Kind**: method  
**Role**: Instance Method

Requests the action to perform its task using the specified input.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
func run(withInput input: Any?) throws -> Any
```

```objc
- (id) runWithInput:(id) input error:(NSError **) error;
```

## Return Value

An [`NSArray`](../../Foundation/nsarray.md) object that contains one or more objects of a data type compatible with a type specified in the receiving action’s `AMProvides` property. If the action doesn’t modify the data passed in `input`, it should return it unchanged. If the action doesn’t have any data to provide, it should return an empty [`NSArray`](../../Foundation/nsarray.md) object.

## Discussion

This method is intended to be overridden.

The input and output objects for actions are usually instances of [`NSArray`](../../Foundation/nsarray.md). If the action encounters problems, it should return by indirection an [`NSError`](../../Foundation/nserror.md) object that describes the error.

## Parameters

- `input`: The input for the receiving action. Should contain one or more objects compatible with one of the types specified in the action’s [`selectedInputType`](./selectedinputtype.md) property.

## See Also

### Controlling the Action
- [func runAsynchronously(withInput: Any?)](./runasynchronously%28withinput%29.md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](./finishrunningwitherror%28_%29.md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](./willfinishrunning%28%29.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](./stop%28%29.md)
  Stops the action from running.
- [func reset()](./reset%28%29.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/run(withinput:))*