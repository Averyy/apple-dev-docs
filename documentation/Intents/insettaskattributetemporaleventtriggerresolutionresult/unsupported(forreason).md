# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object with a resolution that provides a reason the temporal event trigger can’t be applied to the task the user intends to modify.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class func unsupported(forReason reason: INSetTaskAttributeTemporalEventTriggerUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INSetTaskAttributeTemporalEventTriggerUnsupportedReason) reason;
```

## Return Value

A new [`INSetTaskAttributeTemporalEventTriggerResolutionResult`](../insettaskattributetemporaleventtriggerresolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when your app doesn’t support the intent parameter for the specified reason.

## Parameters

- `reason`: The reason that the temporal event trigger is not supported.

## See Also

### Creating a Resolution Result
- [init(temporalEventTriggerResolutionResult: INTemporalEventTriggerResolutionResult)](./init%28temporaleventtriggerresolutionresult%29.md)
  Creates an object with a resolution that successfully matches the specified temporal event.
- [enum INSetTaskAttributeTemporalEventTriggerUnsupportedReason](../insettaskattributetemporaleventtriggerunsupportedreason.md)
  Reasons the app can’t modify the temporal event trigger of the task.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insettaskattributetemporaleventtriggerresolutionresult/unsupported(forreason:))*