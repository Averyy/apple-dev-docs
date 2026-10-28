# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func success(with resolvedCallDestinationType: INCallDestinationType) -> Self
```

```objc
+ (instancetype) successWithResolvedCallDestinationType:(INCallDestinationType) resolvedCallDestinationType;
```

## Return Value

A new [`INCallDestinationTypeResolutionResult`](../incalldestinationtyperesolutionresult.md) object.

## Discussion

Use this method to create a resolution result object when you recognize the specified type of call destination and are able to use it to resolve an intent.

## Parameters

- `resolvedCallDestinationType`: The value that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INCallDestinationType) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incalldestinationtyperesolutionresult/success(with:))*