# PKAutomaticReloadPaymentSummaryItem

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that defines a summary item for an automatic reload or refill payment, such as a store card top-up.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class PKAutomaticReloadPaymentSummaryItem
```

#### Overview

[`PKAutomaticReloadPaymentSummaryItem`](pkautomaticreloadpaymentsummaryitem.md) is a subclass of [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) and inherits all properties of the parent class.

Add a summary item of this type to the [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property of a [`PKPaymentRequest`](pkpaymentrequest.md) object to display an automatic reload payment in the summary items on the payment sheet to the user.

To describe an automatic reload payment, set the summary item values as follows:

- Use the [`amount`](pkpaymentsummaryitem/amount.md) property to specify the reload amount when the account balance reaches the threshold amount, [`thresholdAmount`](pkautomaticreloadpaymentsummaryitem/thresholdamount.md).
- Omit the [`type`](pkpaymentsummaryitem/type.md) property. The summary item type is only relevant for the [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) parent class.

## Topics

### Setting the automatic reload threshold
- [var thresholdAmount: NSDecimalNumber](pkautomaticreloadpaymentsummaryitem/thresholdamount.md)
  The balance an account reaches before you apply the automatic reload amount.

## Relationships

### Inherits From
- [PKPaymentSummaryItem](pkpaymentsummaryitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var automaticReloadBilling: PKAutomaticReloadPaymentSummaryItem](pkautomaticreloadpaymentrequest/automaticreloadbilling.md)
  Summary items that contain the top-up amount and balance threshold amount for the automatic reload payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentsummaryitem)*