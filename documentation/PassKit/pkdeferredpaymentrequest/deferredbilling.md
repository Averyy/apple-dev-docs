# deferredBilling

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An object that contains details about the deferred payment.

**Availability**:
- iOS 16.4+
- iPadOS 16.4+
- Mac Catalyst 16.4+
- macOS 13.3+
- visionOS 1.0+

## Declaration

```swift
var deferredBilling: PKDeferredPaymentSummaryItem { get set }
```

```objc
@property (nonatomic, strong) PKDeferredPaymentSummaryItem * deferredBilling;
```

#### Discussion

For example “Pay $2.99 on October 9, 2023.”

## See Also

### Setting payment summary items
- [class PKDeferredPaymentSummaryItem](../pkdeferredpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest/deferredbilling)*