# summaryItems

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of payment summary item objects that the framework presents to people.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var summaryItems: [PKPaymentSummaryItem] { get set }
```

```objc
@property (nonatomic, copy) NSArray<PKPaymentSummaryItem *> * summaryItems;
```

#### Discussion

This array must contain one [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md), which contains the amount the individual receives. This may differ from the total amount withdrawn — for example, if the transfer has an associated fee. The framework displays the amount this [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md) item represents on the main Apple Pay sheet.

This array may contain up to one [`PKInstantFundsOutFeeSummaryItem`](../pkinstantfundsoutfeesummaryitem.md) to represent a fee deducted as part of an instant transfer, if applicable. The framework also presents this fee on the main sheet when you initialize the [`PKDisbursementRequest`](../pkdisbursementrequest.md) with the [`instantFundsOut`](../pkmerchantcapability/instantfundsout.md) capability option.

You can specify other line items (such as fees not associated with an instant transfer) using [`PKPaymentSummaryItem`](../pkpaymentsummaryitem.md).

If you specify multiple summary items, the last item must represent the total of all previous items.

## See Also

### Setting the summary items
- [class PKPaymentSummaryItem](../pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKDisbursementSummaryItem](../pkdisbursementsummaryitem.md)
  A summary item that represents a disbursement.
- [class PKInstantFundsOutFeeSummaryItem](../pkinstantfundsoutfeesummaryitem.md)
  A summary item that represents a fee for an instant funds out transfer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/summaryitems)*