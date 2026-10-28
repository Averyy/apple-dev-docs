# init(temporalEventTriggerResolutionResult:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Creates an object with a resolution that successfully matches the specified temporal event.

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

## Return Value

A new [`INSetTaskAttributeTemporalEventTriggerResolutionResult`](../insettaskattributetemporaleventtriggerresolutionresult.md) object or nil if the object could not be created.

## Discussion

Use this method to create a result object when you’re able to resolve the temporal event trigger for the user’s intent.

## Parameters

- `temporalEventTriggerResolutionResult`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result
- [class func unsupported(forReason: INSetTaskAttributeTemporalEventTriggerUnsupportedReason) -> Self](./unsupported%28forreason%29.md)
  Creates an object with a resolution that provides a reason the temporal event trigger can’t be applied to the task the user intends to modify.
- [enum INSetTaskAttributeTemporalEventTriggerUnsupportedReason](../insettaskattributetemporaleventtriggerunsupportedreason.md)
  Reasons the app can’t modify the temporal event trigger of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributetemporaleventtriggerresolutionresult/init(temporaleventtriggerresolutionresult:))*