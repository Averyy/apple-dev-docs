# INPaymentMethodResolutionResult

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Describes the result of resolving a payment method.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INPaymentMethodResolutionResult
```

```objc
@interface INPaymentMethodResolutionResult : INIntentResolutionResult
```

#### Overview

An [`INPaymentMethodResolutionResult`](./inpaymentmethodresolutionresult.md) object is what you return when resolving parameters containing an [`INPaymentMethod`](./inpaymentmethod.md) object. Use the creation method that best reflects your ability to successfully resolve the parameter. For additional resolution options, see [`INIntentResolutionResult`](./inintentresolutionresult.md).

## Topics

### Creating a Resolution Result Object
- [class func confirmationRequired(with: INPaymentMethod?) -> Self](./inpaymentmethodresolutionresult/confirmationrequired%28with%29.md)
  Creates an object whose resolution requires that the user must confirm the value before proceeding.
- [class func disambiguation(with: [INPaymentMethod]) -> Self](./inpaymentmethodresolutionresult/disambiguation%28with%29.md)
  Creates an object whose resolution requires the user to select from among the specified objects.
- [class func success(with: INPaymentMethod) -> Self](./inpaymentmethodresolutionresult/success%28with%29.md)
  Creates an object whose resolution involves the successful matching of the specified parameter.

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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inpaymentmethodresolutionresult)*