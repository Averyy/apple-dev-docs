# init(temporalEventTriggerResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object whose resolution successfully matches the specified temporal event.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)
```

```objc
- (instancetype) initWithTemporalEventTriggerResolutionResult:(INTemporalEventTriggerResolutionResult *) temporalEventTriggerResolutionResult;
```

#### Return Value

A new [`INAddTasksTemporalEventTriggerResolutionResult`](../inaddtaskstemporaleventtriggerresolutionresult.md) object or nil if the object could not be created.

#### Discussion

Use this method to create a result object when you’re able to resolve the temporal event trigger for the user’s intent.

## Parameters

- `temporalEventTriggerResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INAddTasksTemporalEventTriggerUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object whose resolution provides a reason why the temporal event trigger cannot be applied to the task the user intends to create.
- [enum INAddTasksTemporalEventTriggerUnsupportedReason](../inaddtaskstemporaleventtriggerunsupportedreason.md)
  Reasons the app can’t create a task with a particular temporal event trigger.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaddtaskstemporaleventtriggerresolutionresult/init(temporaleventtriggerresolutionresult:))*