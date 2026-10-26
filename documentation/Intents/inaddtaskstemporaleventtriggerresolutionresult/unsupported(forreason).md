# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution provides a reason why the temporal event trigger cannot be applied to the task the user intends to create.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class func unsupported(forReason reason: INAddTasksTemporalEventTriggerUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INAddTasksTemporalEventTriggerUnsupportedReason) reason;
```

#### Return Value

A new [`INAddTasksTemporalEventTriggerResolutionResult`](../inaddtaskstemporaleventtriggerresolutionresult.md) object.

#### Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that the temporal event trigger is not supported.

## See Also

### Creating a Resolution Result
- [init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)](./init%28temporaleventtriggerresolutionresult%29.md)
  Creates an object whose resolution successfully matches the specified temporal event.
- [enum INAddTasksTemporalEventTriggerUnsupportedReason](../inaddtaskstemporaleventtriggerunsupportedreason.md)
  Reasons the app can’t create a task with a particular temporal event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstemporaleventtriggerresolutionresult/unsupported(forreason:))*