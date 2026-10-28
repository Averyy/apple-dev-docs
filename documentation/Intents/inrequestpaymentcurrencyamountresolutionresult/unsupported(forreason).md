# unsupported(forReason:)

**Framework**: Intents  
**Kind**: method  
**Role**: Type Method

Creates an object whose resolution indicates that the specified value is not supported.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
class func unsupported(forReason reason: INRequestPaymentCurrencyAmountUnsupportedReason) -> Self
```

```objc
+ (instancetype) unsupportedForReason:(INRequestPaymentCurrencyAmountUnsupportedReason) reason;
```

## Return Value

A new [`INRequestPaymentCurrencyAmountResolutionResult`](../inrequestpaymentcurrencyamountresolutionresult.md) object.

## Discussion

Use this method when the specified currency amount does not met the payment criteria for your service. For example, you might specify this value when the user requests money in an unsupported currency or the request exceeds the maximum transfer limit for the user’s account.

## Parameters

- `reason`: The reason why the currency amount is unsupported. For a list of possible values, see [`INRequestPaymentCurrencyAmountUnsupportedReason`](../inrequestpaymentcurrencyamountunsupportedreason.md).

## See Also

### Creating a Resolution Result Object
- [enum INRequestPaymentCurrencyAmountUnsupportedReason](../inrequestpaymentcurrencyamountunsupportedreason.md)
  Constants indicating the reason for being unable to resolve the currency amount.
- [init(currencyAmountResolutionResult: INCurrencyAmountResolutionResult)](./init%28currencyamountresolutionresult%29.md)
  Creates a resolution result object with the specified currency amount resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentcurrencyamountresolutionresult/unsupported(forreason:))*