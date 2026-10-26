# INAccountTypeResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for account types.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INAccountTypeResolutionResult
```

```objc
@interface INAccountTypeResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INAccountTypeResolutionResult`](./inaccounttyperesolutionresult.md) object is what you return when resolving parameters containing an [`INAccountType`](./inaccounttype.md) value. Use the creation method that best reflects your ability to resolve the parameter.

For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func success(with: INAccountType) -> Self](./inaccounttyperesolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified attribute.
- [class func confirmationRequired(with: INAccountType) -> Self](./inaccounttyperesolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [+ successWithResolvedValue:](./inaccounttyperesolutionresult/successwithresolvedvalue_.md)
- [+ confirmationRequiredWithValueToConfirm:](./inaccounttyperesolutionresult/confirmationrequiredwithvaluetoconfirm_.md)

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
- [class INPaymentStatusResolutionResult](./inpaymentstatusresolutionresult.md)
  A resolution result for the payment status of a bill during a search.
- [class INRequestPaymentCurrencyAmountResolutionResult](./inrequestpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount associated with a payment request.
- [class INRequestPaymentPayerResolutionResult](./inrequestpaymentpayerresolutionresult.md)
  A resolution result for the person making the payment.
- [class INSendPaymentCurrencyAmountResolutionResult](./insendpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount to send to another user.
- [class INSendPaymentPayeeResolutionResult](./insendpaymentpayeeresolutionresult.md)
  A resolution result for the recipient of a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inaccounttyperesolutionresult)*