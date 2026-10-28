# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to confirm the value before proceeding.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class func confirmationRequired(with temporalEventTriggerTypeOptionsToConfirm: INTemporalEventTriggerTypeOptions = []) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTemporalEventTriggerTypeOptionsToConfirm:(INTemporalEventTriggerTypeOptions) temporalEventTriggerTypeOptionsToConfirm;
```

## Return Value

A new [`INTemporalEventTriggerTypeOptionsResolutionResult`](../intemporaleventtriggertypeoptionsresolutionresult.md) object.

## Discussion

Use this method when you can’t resolve the parameter to a similar but not equal temporal event type than the one specified in the intent. Don’t use this method to resolve temporal event types that your app doesn’t support.

## Parameters

- `temporalEventTriggerTypeOptionsToConfirm`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTemporalEventTriggerTypeOptions) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves successfully matching the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggertypeoptionsresolutionresult/confirmationrequired(with:))*