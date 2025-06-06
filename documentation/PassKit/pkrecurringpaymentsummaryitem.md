# PKRecurringPaymentSummaryItem

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PKRecurringPaymentSummaryItem
```

#### Overview

[`PKRecurringPaymentSummaryItem`](pkrecurringpaymentsummaryitem.md) is a subclass of [`PKPaymentSummaryItemType`](pkpaymentsummaryitemtype.md) and inherits all properties of the parent class.

Add a summary item of this type to the [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md) property of a [`PKPaymentRequest`](pkpaymentrequest.md) to display to the user a recurring payment in the summary items on the payment sheet.

To describe a recurring payment, set the summary item values as follows:

- In the [`amount`](pkpaymentsummaryitem/amount.md) property, provide the billing amount for the set interval, for example, the amount charged per week if the [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md) is a week.
- Omit the [`type`](pkpaymentsummaryitem/type.md) property. The summary item type is only relevant for the [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) parent class.
- Set the [`startDate`](pkrecurringpaymentsummaryitem/startdate.md) and [`endDate`](pkrecurringpaymentsummaryitem/enddate.md) to represent the term for the recurring payments, as appropriate.
- Set the [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md), [`intervalCount`](pkrecurringpaymentsummaryitem/intervalcount.md), and [`endDate`](pkrecurringpaymentsummaryitem/enddate.md) to specify a number of repeating payments.

For example, the following code shows a summary item that specifies six monthly payments that start on the transaction date:

```swift
let recurringPayment = PKRecurringPaymentSummaryItem(label: "Total Payment",                                                  NSDecimalNumber(string: "199.99"))

// Payment starts today.
recurringPayment.startDate = nil

// Pay once a month.
recurringPayment.intervalUnit = .month
recurringPayment.intervalCount = 1

// Make 5 more payments for a total of 6 payments.
var dateComponent = DateComponents()
dateComponent.month = 5
recurringPayment.endDate = Calendar.current.date(byAdding: dateComponent, Date())
```

The payment interval is a combination of the [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md) and the [`intervalCount`](pkrecurringpaymentsummaryitem/intervalcount.md). For example, if you set the [`intervalUnit`](pkrecurringpaymentsummaryitem/intervalunit.md) to .[`month`](https://developer.apple.com/documentation/CoreFoundation/CFCalendarUnit/month) and [`intervalCount`](pkrecurringpaymentsummaryitem/intervalcount.md) to `3`, then the payment interval is three months.

## Topics

### Setting the payment period
- [var startDate: Date?](pkrecurringpaymentsummaryitem/startdate.md)
  The date of the first payment.
- [var endDate: Date?](pkrecurringpaymentsummaryitem/enddate.md)
  The date of the final payment.
### Setting the payment interval
- [var intervalUnit: NSCalendar.Unit](pkrecurringpaymentsummaryitem/intervalunit.md)
  The amount of time – in calendar units such as day, month, or year – that represents a fraction of the total payment interval.
- [var intervalCount: Int](pkrecurringpaymentsummaryitem/intervalcount.md)
  The number of interval units that make up the total payment interval.

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

- [var paymentSummaryItems: [PKPaymentSummaryItem]](pkpaymentrequest/paymentsummaryitems.md)
  An array of payment summary item objects that summarize the amount of the payment.
- [class PKPaymentSummaryItem](pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkrecurringpaymentsummaryitem)*