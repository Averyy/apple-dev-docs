# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func success(with resolvedSpatialEventTrigger: INSpatialEventTrigger) -> Self
```

```objc
+ (instancetype) successWithResolvedSpatialEventTrigger:(INSpatialEventTrigger *) resolvedSpatialEventTrigger;
```

## Return Value

A new [`INSpatialEventTriggerResolutionResult`](../inspatialeventtriggerresolutionresult.md) object.

## Discussion

Use this method to create a result object when you successfully identify the trigger object to modify. Provide an [`INSpatialEventTrigger`](../inspatialeventtrigger.md) object with as much information about the trigger conditions as you have available.

## Parameters

- `resolvedSpatialEventTrigger`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INSpatialEventTrigger?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires confirmation from the user before proceeding.
- [class func disambiguation(with: [INSpatialEventTrigger]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inspatialeventtriggerresolutionresult/success(with:))*