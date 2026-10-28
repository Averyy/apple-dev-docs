# resolveTemporalEventTrigger(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the time-based trigger associated with the new tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use [`resolveTemporalEventTrigger(for:with:)`](./resolvetemporaleventtrigger%28for,with%29-7yrz3.md) instead.

## Declaration

```swift
optional func resolveTemporalEventTrigger(for intent: INAddTasksIntent, with completion: @escaping @Sendable (INTemporalEventTriggerResolutionResult) -> Void)
```

```swift
optional func resolveTemporalEventTrigger(for intent: INAddTasksIntent) async -> INTemporalEventTriggerResolutionResult
```

```objc
- (void) resolveTemporalEventTriggerForAddTasks:(INAddTasksIntent *) intent withCompletion:(void (^)(INTemporalEventTriggerResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any time-based triggers associated with the new tasks. Use the intent object to obtain the trigger information, if any, suggested by the user. If the intent doesn’t contain any trigger information, and you don’t require any, return a [`notRequired()`](../inintentresolutionresult/notrequired%28%29.md) resolution.

## Parameters

- `intent`: Details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: Details of your proposed resolution. For successful resolutions, create a resolution object with the [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object representing the trigger that you intend to use.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INAddTasksTargetTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2er0u.md)
  Resolves the task list to receive the new tasks.
- [func resolveTaskTitles(for: INAddTasksIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvetasktitles%28for,with%29.md)
  Resolves the titles for the tasks.
- [func resolveSpatialEventTrigger(for: INAddTasksIntent, with: (INSpatialEventTriggerResolutionResult) -> Void)](./resolvespatialeventtrigger%28for,with%29.md)
  Resolves the location-based trigger associated with the new tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INAddTasksTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-7yrz3.md)
  Resolves the time-based trigger associated with the new tasks.
- [func resolvePriority(for: INAddTasksIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvepriority%28for,with%29.md)
  Resolves the priority associated with the new tasks.
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2uevx.md)
  Called when it is time for you to resolve the task list to receive the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/resolvetemporaleventtrigger(for:with:)-2h9ff)*