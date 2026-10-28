# resolvePriority(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the priority associated with the new tasks.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
optional func resolvePriority(for intent: INAddTasksIntent, with completion: @escaping @Sendable (INTaskPriorityResolutionResult) -> Void)
```

```swift
optional func resolvePriority(for intent: INAddTasksIntent) async -> INTaskPriorityResolutionResult
```

```objc
- (void) resolvePriorityForAddTasks:(INAddTasksIntent *) intent withCompletion:(void (^)(INTaskPriorityResolutionResult *resolutionResult)) completion;
```

## Discussion

This method resolves any priorities associated with the new tasks. Use the intent object to obtain the priority information, if any, suggested by the user. If the intent does not contain any priority information, and you don’t require any, return a resolution indicating that you don’t require a value.

## Parameters

- `intent`: The intent object that contains details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler while implementing this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object that containts the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object that represents the trigger that you intend to use.

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
- [func resolveTargetTaskList(for: INAddTasksIntent, with: (INTaskListResolutionResult) -> Void)](./resolvetargettasklist%28for,with%29-2uevx.md)
  Called when it is time for you to resolve the task list to receive the new tasks.
- [func resolveTemporalEventTrigger(for: INAddTasksIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-2h9ff.md)
  Resolves the time-based trigger associated with the new tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtasksintenthandling/resolvepriority(for:with:))*