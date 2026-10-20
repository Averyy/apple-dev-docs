# paymentSummaryItems

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The list of payment summary items for the instance.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var paymentSummaryItems: [PKPaymentSummaryItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<PKPaymentSummaryItem *> * paymentSummaryItems;
```

## See Also

### Updating summary items
- [class PKPaymentSummaryItem](../pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequestupdate/paymentsummaryitems)*