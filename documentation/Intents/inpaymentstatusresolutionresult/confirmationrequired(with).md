# confirmationRequired(with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution requires that the user confirm the value before proceeding.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class func confirmationRequired(with paymentStatusToConfirm: INPaymentStatus) -> Self
```

```objc
+ (instancetype) confirmationRequiredWithPaymentStatusToConfirm:(INPaymentStatus) paymentStatusToConfirm;
```

#### Return Value

A new [`INPaymentStatusResolutionResult`](../inpaymentstatusresolutionresult.md) object.

#### Discussion

Use this method when you can resolve the parameter to a single value but want the user to confirm that value. For example, you might use this method if you cannot search based on the requested payment status but can search based on another value.

## Parameters

- `paymentStatusToConfirm`: The value that resolves the request but that must be confirmed by the user.

## See Also

### Creating a Resolution Result Object
- [class func success(with: INPaymentStatus) -> Self](./success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatusresolutionresult/confirmationrequired(with:))*