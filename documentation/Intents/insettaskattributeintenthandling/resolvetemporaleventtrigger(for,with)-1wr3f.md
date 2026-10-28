# resolveTemporalEventTrigger(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the time-based trigger to apply to the task.

**Availability**:
- iOS 11.0+ - Deprecated in 27.0
- iPadOS 11.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 4.0+ - Deprecated in 27.0

> **Deprecated**: Use [`resolveTemporalEventTrigger(for:with:)`](./resolvetemporaleventtrigger%28for,with%29-9bfly.md) instead.

## Declaration

```swift
optional func resolveTemporalEventTrigger(for intent: INSetTaskAttributeIntent, with completion: @escaping @Sendable (INTemporalEventTriggerResolutionResult) -> Void)
```

```swift
optional func resolveTemporalEventTrigger(for intent: INSetTaskAttributeIntent) async -> INTemporalEventTriggerResolutionResult
```

```objc
- (void) resolveTemporalEventTriggerForSetTaskAttribute:(INSetTaskAttributeIntent *) intent withCompletion:(void (^)(INTemporalEventTriggerResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the time-based trigger to apply to the task. For apps that support reminders based on the current time, use this method to resolve the trigger information. If time-based reminders are optional, return a successful resolution when the user provides trigger information or return a [`notRequired()`](../inintentresolutionresult/notrequired%28%29.md) resolution when there’s no trigger information. If the intent includes some trigger information, but not enough for a successful resolution, you can ask the user to confirm or disambiguate from among the possible values.

## Parameters

- `intent`: Details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: Details of your proposed resolution. For successful resolutions, create a resolution object with the [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object that you intend to apply to the task.

## See Also

### Resolving the Intent Parameters
- [func resolveTargetTask(for: INSetTaskAttributeIntent, with: (INTaskResolutionResult) -> Void)](./resolvetargettask%28for,with%29.md)
  Resolves which task the user wants to modify.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling/resolvetemporaleventtrigger(for:with:)-1wr3f)*