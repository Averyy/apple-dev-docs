# INRequestPaymentCurrencyAmountResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A resolution result for the currency amount associated with a payment request.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class INRequestPaymentCurrencyAmountResolutionResult
```

```objc
@interface INRequestPaymentCurrencyAmountResolutionResult : INCurrencyAmountResolutionResult
```

## Overview

An [`INRequestPaymentCurrencyAmountResolutionResult`](./inrequestpaymentcurrencyamountresolutionresult.md) object is what you return when resolving parameters containing an [`INCurrencyAmount`](./incurrencyamount.md) value. Use the creation method that best reflects your ability to resolve the parameter successfully.

For additional resolution options, see [`INCurrencyAmountResolutionResult`](./incurrencyamountresolutionresult.md) and [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func unsupported(forReason: INRequestPaymentCurrencyAmountUnsupportedReason) -> Self](./inrequestpaymentcurrencyamountresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [enum INRequestPaymentCurrencyAmountUnsupportedReason](./inrequestpaymentcurrencyamountunsupportedreason.md)
  Constants indicating the reason for being unable to resolve the currency amount.
- [init(currencyAmountResolutionResult: INCurrencyAmountResolutionResult)](./inrequestpaymentcurrencyamountresolutionresult/init%28currencyamountresolutionresult%29.md)
  Creates a resolution result object with the specified currency amount resolution result object.

## Relationships

### Inherits From
- [INCurrencyAmountResolutionResult](./incurrencyamountresolutionresult.md)
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
- [class INPaymentStatusResolutionResult](./inpaymentstatusresolutionresult.md)
  A resolution result for the payment status of a bill during a search.
- [class INRequestPaymentPayerResolutionResult](./inrequestpaymentpayerresolutionresult.md)
  A resolution result for the person making the payment.
- [class INSendPaymentCurrencyAmountResolutionResult](./insendpaymentcurrencyamountresolutionresult.md)
  A resolution result for the currency amount to send to another user.
- [class INSendPaymentPayeeResolutionResult](./insendpaymentpayeeresolutionresult.md)
  A resolution result for the recipient of a payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentcurrencyamountresolutionresult)*