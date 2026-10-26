# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires confirmation from the user before proceeding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func confirmationRequired(with temporalEventTriggerToConfirm: INTemporalEventTrigger?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithTemporalEventTriggerToConfirm:(INTemporalEventTrigger *) temporalEventTriggerToConfirm;
```

#### Return Value

A new [`INTemporalEventTriggerResolutionResult`](../intemporaleventtriggerresolutionresult.md) object.

#### Discussion

Use this method when you have to make assumptions about the time information specified by the user. Provide an [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object with the trigger details as you intend to apply them.

## Parameters

- `temporalEventTriggerToConfirm`: The object that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTemporalEventTrigger) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func disambiguation(with: [INTemporalEventTrigger]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggerresolutionresult/confirmationrequired(with:))*