# HMError.Code.noActionsInActionSet

**Framework**: HomeKit  
**Kind**: case  
**Role**: Case

An attempt to execute an action set with no actions.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case noActionsInActionSet
```

```c
HMErrorCodeNoActionsInActionSet
```

## See Also

### Action set errors
- [HMError.Code.actionInAnotherActionSet](./actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [HMError.Code.actionSetExecutionFailed](./actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [HMError.Code.actionSetExecutionInProgress](./actionsetexecutioninprogress.md)
  An error indicating the execution of the action set is in progress.
- [HMError.Code.actionSetExecutionPartialSuccess](./actionsetexecutionpartialsuccess.md)
  An attempt to execute the action set was only partially successful.
- [HMError.Code.cannotRemoveBuiltinActionSet](./cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [HMError.Code.noRegisteredActionSets](./noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/code/noactionsinactionset)*