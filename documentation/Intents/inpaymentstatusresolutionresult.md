# INPaymentStatusResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the payment status of a bill during a search.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INPaymentStatusResolutionResult
```

```objc
@interface INPaymentStatusResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INPaymentStatusResolutionResult`](./inpaymentstatusresolutionresult.md) object is what you return when resolving parameters containing an [`INPaymentStatus`](./inpaymentstatus.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INPaymentStatus) -> Self](./inpaymentstatusresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified value.
- [class func confirmationRequired(with: INPaymentStatus) -> Self](./inpaymentstatusresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user confirm the value before proceeding.
- [+ successWithResolvedValue:](./inpaymentstatusresolutionresult/successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./inpaymentstatusresolutionresult/confirmationrequiredwithvaluetoconfirm_.md)

## Relationships

### Inherits From
- [INIntentResolutionResult](./inintentresolutionresult.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resolution Results
- [class INAccountTypeResolutionResult](./inaccounttyperesolutionresult.md)
  A resolution result for account types.
- [class INBalanceTypeResolutionResult](./inbalancetyperesolutionresult.md)
  A resolution result for balance types.
- [class INCurrencyAmountResolutionResult](./incurrencyamountresolutionresult.md)
  A resolution result for a currency amount associated with an intent.
- [class INPaymentAccountResolutionResult](./inpaymentaccountresolutionresult.md)
  A resolution result for the user account that provides the funds to pay a bill.
- [class INPaymentAmountResolutionResult](./inpaymentamountresolutionresult.md)
  A resolution result for the amount to pay for a bill.
- [class INPaymentMethodResolutionResult](./inpaymentmethodresolutionresult.md)
  Describes the result of resolving a payment method.
- [class INRequestPaymentCurrencyAmountResolutionResult](./inrequestpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount associated with a payment request.
- [class INRequestPaymentPayerResolutionResult](./inrequestpaymentpayerresolutionresult.md)
  A resolution result for the person making the payment.
- [class INSendPaymentCurrencyAmountResolutionResult](./insendpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount to send to another user.
- [class INSendPaymentPayeeResolutionResult](./insendpaymentpayeeresolutionresult.md)
  A resolution result for the recipient of a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentstatusresolutionresult)*