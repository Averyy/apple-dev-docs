# resolvePriority(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the intended priority of the task.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
optional func resolvePriority(for intent: INSetTaskAttributeIntent, with completion: @escaping @Sendable (INTaskPriorityResolutionResult) -> Void)
```

```swift
optional func resolvePriority(for intent: INSetTaskAttributeIntent) async -> INTaskPriorityResolutionResult
```

```objc
- (void) resolvePriorityForSetTaskAttribute:(INSetTaskAttributeIntent *) intent withCompletion:(void (^)(INTaskPriorityResolutionResult *resolutionResult)) completion;
```

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
- [func resolveTaskTitle(for: INSetTaskAttributeIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolvetasktitle%28for,with%29.md)
  Resolves the intended title of the task.
- [func resolveTemporalEventTrigger(for: INSetTaskAttributeIntent, with: (INTemporalEventTriggerResolutionResult) -> Void)](./resolvetemporaleventtrigger%28for,with%29-1wr3f.md)
  Resolves the time-based trigger to apply to the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributeintenthandling/resolvepriority(for:with:))*