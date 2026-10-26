# disambiguation(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires the user to select from among the specified objects.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func disambiguation(with paymentMethodsToDisambiguate: [INPaymentMethod]) -> Self
```

```objc
+ (instancetype) disambiguationWithPaymentMethodsToDisambiguate:(NSArray<INPaymentMethod *> *) paymentMethodsToDisambiguate;
```

#### Return Value

A new `INPaymentMethodResolutionResult` object.

#### Discussion

Use this method to create a result object when there’s more one value that might match the given parameter. Siri asks the user to select from among the objects you provide.

## Parameters

- `paymentMethodsToDisambiguate`: An array of [`INPaymentMethod`](../inpaymentmethod.md) objects for the user to choose from.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentMethod?) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func success(with: INPaymentMethod) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethodresolutionresult/disambiguation(with:))*