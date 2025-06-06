# paymentSummaryItems

**Framework**: Passkit  
**Kind**: property

An array of payment summary item objects that summarize the amount of the payment.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var paymentSummaryItems: [PKPaymentSummaryItem] { get set }
```

#### Discussion

A typical transaction includes separate summary items for the order total, shipping cost, tax, and the grand total. See the following code for an example.

Apple Pay uses the last item in the `paymentSummaryItems` array as the grand total for the purchase shown in the example in [`paymentSummaryItems`](pkpaymentrequest/paymentsummaryitems.md). The [`PKPaymentAuthorizationViewController`](pkpaymentauthorizationviewcontroller.md) class displays this item differently than the rest of the summary items. As a result, there are additional requirements placed on both its amount and its label.

- Set the grand total amount to the sum of all the other items in the array. This amount must be greater than or equal to zero.
- Set the grand total label to the name of your company. This label represents the person or company receiving payment.

Your payment processor might have additional requirements, such as a minimum or maximum payment amount.

In iOS 15 and later you can create three different types of payment summary items:

- Use a [`PKPaymentSummaryItem`](pkpaymentsummaryitem.md) for an immediate payment.
- Use a [`PKDeferredPaymentSummaryItem`](pkdeferredpaymentsummaryitem.md) for a payment that occurs in the future, such as a pre-order.
- Use a [`PKRecurringPaymentSummaryItem`](pkrecurringpaymentsummaryitem.md) for a payment that occurs more than once, such as a subscription.

> **Note**:  In versions of iOS prior to version 12.0 and watchOS prior to version 5.0, the amount of the grand total must be greater than zero.

Setting the payment summary items:

```objc
// 12.75 subtotal
NSDecimalNumber *subtotalAmount = [NSDecimalNumber decimalNumberWithMantissa:1275
 exponent:-2 isNegative:NO];
self.subtotal = [PKPaymentSummaryItem summaryItemWithLabel:@"Subtotal" amount:subtotalAmount];
 
// 2.00 discount
NSDecimalNumber *discountAmount = [NSDecimalNumber decimalNumberWithMantissa:200 exponent:-2 isNegative:YES];
self.discount = [PKPaymentSummaryItem summaryItemWithLabel:@"Discount" amount:discountAmount];
 
// 12.75 - 2.00 = 10.75 grand total
NSDecimalNumber *totalAmount = [NSDecimalNumber zero];
totalAmount = [totalAmount decimalNumberByAdding:subtotalAmount];
totalAmount = [totalAmount decimalNumberByAdding:discountAmount];
self.total = [PKPaymentSummaryItem summaryItemWithLabel:@"My Company Name" amount:totalAmount];
self.summaryItems = @[self.subtotal, self.discount, self.total];
request.paymentSummaryItems = self.summaryItems;
```

## See Also

- [convenience init(label: String, amount: NSDecimalNumber)](pkpaymentsummaryitem/init(label:amount:).md)
  Initializes and returns a summary item with the given label and amount.
- [class PKPaymentSummaryItem](pkpaymentsummaryitem.md)
  An object that defines a summary item in a payment request, taxes, discounts, shipping, a grand total, and the like.
- [class PKRecurringPaymentSummaryItem](pkrecurringpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs repeatedly at a specified interval, such as a subscription.
- [class PKDeferredPaymentSummaryItem](pkdeferredpaymentsummaryitem.md)
  An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentrequest/paymentsummaryitems)*