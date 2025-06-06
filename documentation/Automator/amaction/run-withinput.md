# run(withInput:)

**Framework**: Automator  
**Kind**: method

Requests the action to perform its task using the specified input.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.7+

## Declaration

```swift
func run(withInput input: Any?) throws -> Any
```

#### Return Value

An [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) object that contains one or more objects of a data type compatible with a type specified in the receiving action’s `AMProvides` property. If the action doesn’t modify the data passed in `input`, it should return it unchanged. If the action doesn’t have any data to provide, it should return an empty [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray) object.

#### Discussion

This method is intended to be overridden.

The input and output objects for actions are usually instances of [`NSArray`](https://developer.apple.com/documentation/Foundation/NSArray). If the action encounters problems, it should return by indirection an [`NSError`](https://developer.apple.com/documentation/Foundation/NSError) object that describes the error.

## Parameters

- `input`: The input for the receiving action. Should contain one or more objects compatible with one of the types specified in the action’s   property.

## See Also

- [func runAsynchronously(withInput: Any?)](amaction/runasynchronously(withinput:).md)
  Causes Automator to wait for notification that the action has completed execution, which allows the action to perform an asynchronous operation.
- [func finishRunningWithError((any Error)?)](amaction/finishrunningwitherror(_:).md)
  Causes the action to stop running and return an error, which, in turn, causes the workflow to stop.
- [func willFinishRunning()](amaction/willfinishrunning.md)
  Provides an opportunity for an action to perform cleanup operations, such as closing windows and deallocating memory.
- [func stop()](amaction/stop.md)
  Stops the action from running.
- [func reset()](amaction/reset.md)
  Resets the action to its initial state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/automator/amaction/run(withinput:))*