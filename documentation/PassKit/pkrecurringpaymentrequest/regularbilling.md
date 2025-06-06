# regularBilling

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var regularBilling: PKRecurringPaymentSummaryItem { get set }
```

## See Also

- [var trialBilling: PKRecurringPaymentSummaryItem?](pkrecurringpaymentrequest/trialbilling.md)
  The trial billing cycle for the recurring payment.
- [class PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest/regularbilling)*