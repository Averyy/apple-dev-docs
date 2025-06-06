# trialBilling

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The trial billing cycle for the recurring payment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var trialBilling: PKRecurringPaymentSummaryItem? { get set }
```

#### Discussion

The trial billing cycle is optional; use it if the purchase has a trial period.

## See Also

- [var regularBilling: PKRecurringPaymentSummaryItem](pkrecurringpaymentrequest/regularbilling.md)
  The regular billing cycle for the recurring payment, including start and end dates, an interval, and an interval count.
- [class PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest/trialbilling)*