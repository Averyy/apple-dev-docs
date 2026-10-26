# INRequestPaymentCurrencyAmountUnsupportedReason

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

Constants indicating the reason for being unable to resolve the currency amount.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum INRequestPaymentCurrencyAmountUnsupportedReason
```

```c
enum INRequestPaymentCurrencyAmountUnsupportedReason : NSInteger;
```

## Topics

### Constants
- [INRequestPaymentCurrencyAmountUnsupportedReason.paymentsAmountBelowMinimum](./inrequestpaymentcurrencyamountunsupportedreason/paymentsamountbelowminimum.md)
  The payment amount is below the minimum transfer amount established by your app.
- [INRequestPaymentCurrencyAmountUnsupportedReason.paymentsAmountAboveMaximum](./inrequestpaymentcurrencyamountunsupportedreason/paymentsamountabovemaximum.md)
  The payment amount exceeds the maximum transfer amount allowed by your app for the user.
- [INRequestPaymentCurrencyAmountUnsupportedReason.paymentsCurrencyUnsupported](./inrequestpaymentcurrencyamountunsupportedreason/paymentscurrencyunsupported.md)
  The payment currency is not supported by your app.
### Initializers
- [init?(rawValue: Int)](./inrequestpaymentcurrencyamountunsupportedreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating a Resolution Result Object
- [class func unsupported(forReason: INRequestPaymentCurrencyAmountUnsupportedReason) -> Self](./inrequestpaymentcurrencyamountresolutionresult/unsupported%28forreason%29.md)
  Creates an object whose resolution indicates that the specified value is not supported.
- [init(currencyAmountResolutionResult: INCurrencyAmountResolutionResult)](./inrequestpaymentcurrencyamountresolutionresult/init%28currencyamountresolutionresult%29.md)
  Creates a resolution result object with the specified currency amount resolution result object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestpaymentcurrencyamountunsupportedreason)*