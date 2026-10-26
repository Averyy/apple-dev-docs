# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves successfully matching the specified parameter.

**Availability**:
- iOS 13.0+ - Deprecated in 27.0
- iPadOS 13.0+ - Deprecated in 27.0
- Mac Catalyst 13.1+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.0
- watchOS 6.0+ - Deprecated in 27.0

## Declaration

```swift
class func success(with resolvedTemporalEventTriggerTypeOptions: INTemporalEventTriggerTypeOptions = []) -> Self
```

```objc
+ (instancetype) successWithResolvedTemporalEventTriggerTypeOptions:(INTemporalEventTriggerTypeOptions) resolvedTemporalEventTriggerTypeOptions;
```

#### Return Value

A new [`INTemporalEventTriggerTypeOptionsResolutionResult`](../intemporaleventtriggertypeoptionsresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you’re able to search through the user’s notes based on a specified temporal trigger event.

## Parameters

- `resolvedTemporalEventTriggerTypeOptions`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INTemporalEventTriggerTypeOptions) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires the user to confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intemporaleventtriggertypeoptionsresolutionresult/success(with:))*