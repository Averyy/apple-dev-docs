# success(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution involves the successful matching of the specified value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func success(with resolvedPaymentStatus: INPaymentStatus) -> Self
```

```objc
+ (instancetype) successWithResolvedPaymentStatus:(INPaymentStatus) resolvedPaymentStatus;
```

#### Return Value

A new [`INPaymentStatusResolutionResult`](../inpaymentstatusresolutionresult.md) object.

#### Discussion

Use this method to create a result object when you are able to perform a search based on the requested payment status.

## Parameters

- `resolvedPaymentStatus`: The value that resolves the requested value of the intent. You may specify a different payment status if your app treats that value as equivalent to the status requested by the user.

## See Also

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentStatus) -> Self](./confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.
- [+ successWithResolvedValue:](./successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./confirmationrequiredwithvaluetoconfirm_.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatusresolutionresult/success(with:))*