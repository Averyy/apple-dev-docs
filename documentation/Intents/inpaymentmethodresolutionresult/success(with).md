# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified parameter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func success(with resolvedPaymentMethod: INPaymentMethod) -> Self
```

```objc
+ (instancetype) successWithResolvedPaymentMethod:(INPaymentMethod *) resolvedPaymentMethod;
```

#### Return Value

A new `INPaymentMethodResolutionResult` object.

#### Discussion

Use this method to create a result object when you’re able to resolve a parameter successfully to a value in your own internal data structures.

## Parameters

- `resolvedPaymentMethod`: The object that resolves the requested parameter of the intent. This value may be different than the one specified in the intent object.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentMethod?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INPaymentMethod]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethodresolutionresult/success(with:))*