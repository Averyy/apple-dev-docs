# resolveTargetTaskList(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the task list to receive the new tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
optional func resolveTargetTaskList(for intent: INAddTasksIntent, with completion: @escaping @Sendable (INAddTasksTargetTaskListResolutionResult) -> Void)
```

```swift
optional func resolveTargetTaskList(for intent: INAddTasksIntent) async -> INAddTasksTargetTaskListResolutionResult
```

```objc
- (void) resolveTargetTaskListForAddTasks:(INAddTasksIntent *) intent completion:(void (^)(INAddTasksTargetTaskListResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve that task list that’s to recieve the new tasks. Use the intent object to obtain the task list, if any, suggested by the user. If the intent doesn’t specify a task list, choose a resolution that’s most appropriate for your app. If you can select a default task list, return a result of success with that task list. If you can’t select a default task list, you might ask the user to provide a value or choose from among a few likely candidates.

## Parameters

- `intent`: Details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: Details of your proposed resolution. For successful resolutions, create a resolution object with the [`INTaskList`](../intasklist.md) object representing the task list that you intend to use.

## See Also

### Resolving the Intent Parameters
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
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-2h9ff.md)
  Resolves the time-based trigger associated with the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/resolvetargettasklist(for:with:)-2er0u)*