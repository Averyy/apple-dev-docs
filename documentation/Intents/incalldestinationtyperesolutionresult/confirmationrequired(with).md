# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user must confirm the value before proceeding.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func confirmationRequired(with callDestinationTypeToConfirm: INCallDestinationType) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithCallDestinationTypeToConfirm:(INCallDestinationType) callDestinationTypeToConfirm;
```

## Return Value

A new [`INCallDestinationTypeResolutionResult`](../incalldestinationtyperesolutionresult.md) object.

## Discussion

Use this method when you can resolve the parameter but want the user to confirm the value before proceeding.

## Parameters

- `callDestinationTypeToConfirm`: The value that resolves the request but must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INCallDestinationType) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/incalldestinationtyperesolutionresult/confirmationrequired(with:))*