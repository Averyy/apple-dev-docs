# HMError.Code.actionSetExecutionInProgress

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

An error indicating the execution of the action set is in progress.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case actionSetExecutionInProgress
```

```c
HMErrorCodeActionSetExecutionInProgress
```

## See Also

### Action set errors
- [HMError.Code.actionInAnotherActionSet](./actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [HMError.Code.actionSetExecutionFailed](./actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [HMError.Code.actionSetExecutionPartialSuccess](./actionsetexecutionpartialsuccess.md)
  An attempt to execute the action set was only partially successful.
- [HMError.Code.cannotRemoveBuiltinActionSet](./cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [HMError.Code.noActionsInActionSet](./noactionsinactionset.md)
  An attempt to execute an action set with no actions.
- [HMError.Code.noRegisteredActionSets](./noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code/actionsetexecutioninprogress)*