# resolveTargetTask(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves which task the user wants to modify.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveTargetTask(for intent: INSetTaskAttributeIntent, with completion: @escaping @Sendable (INTaskResolutionResult) -> Void)
```

```swift
optional func resolveTargetTask(for intent: INSetTaskAttributeIntent) async -> INTaskResolutionResult
```

```objc
- (void) resolveTargetTaskForSetTaskAttribute:(INSetTaskAttributeIntent *) intent withCompletion:(void (^)(INTaskResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the task that the user wants to modify. Use the intent object to obtain information about the task that the user wants to modify. Use the information in the [`INTask`](../intask.md) object to look up the corresponding task information in your app’s data structures. Return a resolution that includes as much information about the task as you have available.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INTask`](../intask.md) object that you intend to modify.

## See Also

### Resolving the Intent Parameters
- [func resolveStatus(for: INSetTaskAttributeIntent, with: (INTaskStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the intended status of the task.
- [func resolveSpatialEventTrigger(for: INSetTaskAttributeIntent, with: (INSpatialEventTriggerResolutionResult) -> Void)](./resolvespatialeventtrigger%28for,with%29.md)
  Resolves the location-based trigger to apply to the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INSetTaskAttributeTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-9bfly.md)
  Resolves the time-based trigger to apply to the task.
- [func resolvePriority(for: INSetTaskAttributeIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvepriority%28for,with%29.md)
  Resolves the intended priority of the task.
- [func resolveTaskTitle(for: INSetTaskAttributeIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetasktitle%28for,with%29.md)
  Resolves the intended title of the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-1wr3f.md)
  Resolves the time-based trigger to apply to the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling/resolvetargettask(for:with:))*