# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func disambiguation(with temporalEventTriggersToDisambiguate: [INTemporalEventTrigger]) -> Self
```

```objc
+ (instancetype) disambiguationWithTemporalEventTriggersToDisambiguate:(NSArray<INTemporalEventTrigger *> *) temporalEventTriggersToDisambiguate;
```

#### Return Value

A new [`INTemporalEventTriggerResolutionResult`](../intemporaleventtriggerresolutionresult.md) object.

#### Discussion

Use this method to create a result object when more than one trigger condition matches the provided information and you cannot pick one definitively. Ask the user to select from among the triggers that you specify.

For each [`INTemporalEventTrigger`](../intemporaleventtrigger.md) object that you provide, include enough information to be able to resolve that trigger uniquely later.

## Parameters

- `temporalEventTriggersToDisambiguate`: An array of [`INTemporalEventTrigger`](../intemporaleventtrigger.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INTemporalEventTrigger) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.
- [class func confirmationRequired(with: INTemporalEventTrigger?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggerresolutionresult/disambiguation(with:))*