# actionSetExecutionInProgress

**Framework**: HomeKit  
**Kind**: property

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
static var actionSetExecutionInProgress: HMError.Code { get }
```

## See Also

- [static var actionInAnotherActionSet: HMError.Code](hmerror/actioninanotheractionset.md)
  An attempt to add an action that exists in one action set to another action set.
- [static var actionSetExecutionFailed: HMError.Code](hmerror/actionsetexecutionfailed.md)
  An attempt to execute the action set failed.
- [static var actionSetExecutionPartialSuccess: HMError.Code](hmerror/actionsetexecutionpartialsuccess.md)
  An attempt to execute the action set was only partially successful.
- [static var cannotRemoveBuiltinActionSet: HMError.Code](hmerror/cannotremovebuiltinactionset.md)
  An error indicating the built-in action set cannot be removed.
- [static var noActionsInActionSet: HMError.Code](hmerror/noactionsinactionset.md)
  An attempt to execute an action set with no actions.
- [static var noRegisteredActionSets: HMError.Code](hmerror/noregisteredactionsets.md)
  An attempt to activate a trigger with no action sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmerror/actionsetexecutioninprogress)*