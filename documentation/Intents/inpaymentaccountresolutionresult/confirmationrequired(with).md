# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user confirm the value before proceeding.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with paymentAccountToConfirm: INPaymentAccount?) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithPaymentAccountToConfirm:(INPaymentAccount *) paymentAccountToConfirm;
```

#### Return Value

A new [`INPaymentAccountResolutionResult`](../inpaymentaccountresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to a single value but want the user to confirm that value.

## Parameters

- `paymentAccountToConfirm`: The value that resolves the request but that must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPaymentAccount) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func disambiguation(with: [INPaymentAccount]) -> Self](./disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentaccountresolutionresult/confirmationrequired(with:))*