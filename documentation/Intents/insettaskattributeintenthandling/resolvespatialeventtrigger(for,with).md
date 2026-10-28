# resolveSpatialEventTrigger(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the location-based trigger to apply to the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: INSetTaskAttributeIntentHandling is deprecated. Please adopt the Notes or Reminders AppSchema domain instead.

## Declaration

```swift
optional func resolveSpatialEventTrigger(for intent: INSetTaskAttributeIntent, with completion: @escaping @Sendable (INSpatialEventTriggerResolutionResult) -> Void)
```

```swift
optional func resolveSpatialEventTrigger(for intent: INSetTaskAttributeIntent) async -> INSpatialEventTriggerResolutionResult
```

```objc
- (void) resolveSpatialEventTriggerForSetTaskAttribute:(INSetTaskAttributeIntent *) intent withCompletion:(void (^)(INSpatialEventTriggerResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the location-based trigger to apply to the task. For apps that support reminders based on the user’s proximity to a location, use this method to resolve the trigger information. If location-based reminders are optional, return a successful resolution when the user provided trigger information or return a not required resolution when there is no trigger information. If the intent includes some trigger information, but not enough for a successful resolution, you can ask the user to confirm or disambiguate from among the possible values.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`INSpatialEventTrigger`](../inspatialeventtrigger.md) object that you intend to apply to the task.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetTask(for: INSetTaskAttributeIntent, with: (INTaskResolutionResult) -> Void)](./resolvetargettask%28for,with%29.md)
  Resolves which task the user wants to modify.
- [func resolveStatus(for: INSetTaskAttributeIntent, with: (INTaskStatusResolutionResult) -> Void)](./resolvestatus%28for,with%29.md)
  Resolves the intended status of the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INSetTaskAttributeTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-9bfly.md)
  Resolves the time-based trigger to apply to the task.
- [func resolvePriority(for: INSetTaskAttributeIntent, with: (INTaskPriorityResolutionResult) -> Void)](./resolvepriority%28for,with%29.md)
  Resolves the intended priority of the task.
- [func resolveTaskTitle(for: INSetTaskAttributeIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetasktitle%28for,with%29.md)
  Resolves the intended title of the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-1wr3f.md)
  Resolves the time-based trigger to apply to the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling/resolvespatialeventtrigger(for:with:))*