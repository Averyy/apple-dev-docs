# resolveSpatialEventTrigger(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the location-based trigger associated with the new tasks.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INAddTasksIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveSpatialEventTrigger(for intent: INAddTasksIntent, with completion: @escaping @Sendable (INSpatialEventTriggerResolutionResult) -> Void)
```

```swift
optional func resolveSpatialEventTrigger(for intent: INAddTasksIntent) async -> INSpatialEventTriggerResolutionResult
```

```objc
- (void) resolveSpatialEventTriggerForAddTasks:(INAddTasksIntent *) intent withCompletion:(void (^)(INSpatialEventTriggerResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the location-based trigger associated with the new tasks. Use the intent object to obtain the trigger information, if any, suggested by the user. If the intent doesn’t contain any trigger information, and you do not require any, return a resolution indicating that you do not require a value. If the placemark information in the trigger is insufficient to identify the intended location, you might ask the user to choose from two to five triggers with different locations that match the provided placemark data.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INSpatialEventTrigger`](../inspatialeventtrigger.md) object representing the trigger that you intend to use.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INAddTasksTargetTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2er0u.md)
  Resolves the task list to receive the new tasks.
- [func resolveTaskTitles(for: INAddTasksIntent, with: ([INSpeakableStringResolutionResult]) -> Void)](./resolvetasktitles%28for,with%29.md)
  Resolves the titles for the tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INAddTasksTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-7yrz3.md)
  Resolves the time-based trigger associated with the new tasks.
- [func resolvePriority(for: INAddTasksIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvepriority%28for,with%29.md)
  Resolves the priority associated with the new tasks.
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2uevx.md)
  Called when it is time for you to resolve the task list to receive the new tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-2h9ff.md)
  Resolves the time-based trigger associated with the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/resolvespatialeventtrigger(for:with:))*