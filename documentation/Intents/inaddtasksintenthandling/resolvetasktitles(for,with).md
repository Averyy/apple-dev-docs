# resolveTaskTitles(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the titles for the tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveTaskTitles(for intent: INAddTasksIntent, with completion: @escaping @Sendable ([INSpeakableStringResolutionResult]) -> Void)
```

```swift
optional func resolveTaskTitles(for intent: INAddTasksIntent) async -> [INSpeakableStringResolutionResult]
```

```objc
- (void) resolveTaskTitlesForAddTasks:(INAddTasksIntent *) intent withCompletion:(void (^)(NSArray<INSpeakableStringResolutionResult *> *resolutionResults)) completion;
```

#### Discussion

Implement this method to resolve the titles for the taks. Use the intent object to obtain the titles suggested by the user. If the user doesn’t supply any task titles, return a response that indicates you need a value for the task titles. Alternatively, you could return a successful resolution containing a default task title.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResults**: The details of your proposed resolutions. For successful resolutions, create an array of resolution objects with the title strings to use for the tasks.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INAddTasksTargetTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2er0u.md)
  Resolves the task list to receive the new tasks.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/resolvetasktitles(for:with:))*