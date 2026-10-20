# actionSetExecutionPartialSuccess

**Framework**: HomeKit  
**Kind**: property  
**Role**: Type Property

An attempt to execute the action set was only partially successful.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var actionSetExecutionPartialSuccess: HMError.Code { get }
```

## See Also

### Detecting action set errors
- [static var actionInAnotherActionSet: HMError.Code](./actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [static var actionSetExecutionFailed: HMError.Code](./actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [static var actionSetExecutionInProgress: HMError.Code](./actionsetexecutioninprogress.md)
  An error indicating the execution of the action set is in progress.
- [static var cannotRemoveBuiltinActionSet: HMError.Code](./cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [static var noActionsInActionSet: HMError.Code](./noactionsinactionset.md)
  An attempt to execute an action set with no actions.
- [static var noRegisteredActionSets: HMError.Code](./noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/actionsetexecutionpartialsuccess)*