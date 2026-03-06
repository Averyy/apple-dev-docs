# SubscriptionBuyLineItem

**Framework**: External Purchase Server API  
**Kind**: dictionary

The line item that indicates a subscription-related event or transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object SubscriptionBuyLineItem
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)
- [Reporting corrections](reportcorrections.md)

#### Discussion

Use a `SubscriptionBuyLineItem` to report a subscription-related transaction or event, or a correction to the same.

Each line-item object represents one transaction. Other types of line-item objects include:

- [`OneTimeBuyLineItem`](onetimebuylineitem.md), for reporting a one-time charge
- [`RefundLineItem`](refundlineitem.md), for reporting refunds

Include the line-item objects in the `lineItems` array of an [`ExternalPurchaseReport`](externalpurchasereport.md) object. To send the report, include the [`ExternalPurchaseReport`](externalpurchasereport.md) object in a request to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint.

> **Note**: Identify a subscription using the [`lineItemId`](lineitemid.md) of the original subscription-start transaction. A line item for a subscription start has an [`eventType`](eventtype.md) of `BUY` and a [`subscriptionEvent`](subscriptionevent.md) of `SUBSCRIPTION_START`.

For example, to report a renewal for a subscription, set the renewal transaction’s [`referenceLineItemId`](referencelineitemid.md) to the `lineItemId` of the subscription-start line item, and set the  `subscriptionEvent` to `RENEWAL`.

For more information, see [`Reporting tokens with transactions`](reportwithtransactions.md) and [`Reporting corrections`](reportcorrections.md).

## Properties

- `lineItemId` (lineItemId) *(required)*: A unique identifier for the transaction, that you determine. The value must be unique per app. Using UUIDs is recommended. Reuse a `lineItemId` only to submit a correction for a previously submitted line item.
- `referenceLineItemId` (referenceLineItemId): The [`lineItemId`](lineitemid.md) of initial purchase transaction for the subscription.
- `creationDate` (creationDate) *(required)*: The UNIX date, in milliseconds, that the customer authorized the purchase.
- `restatement` (restatement): Set to `true` to indicate that this line item is correcting (restating) a line item that you previously submitted. For more information, see [`Reporting corrections`](reportcorrections.md).
- `erroneouslySubmitted` (erroneouslySubmitted): Set to `true` to indicate that you previously submitted the line item erroneously. Set the `restatement` field to `true` also. For more information, see [`Reporting corrections`](reportcorrections.md).
- `subscriptionEvent` (subscriptionEvent) *(required)*: The subscription event the transaction represents, including a subscription start, a renewal, a change, or a payment. For more information, see [`subscriptionEvent`](subscriptionevent.md).
- `subscriptionStartDate` (subscriptionStartDate) *(required)*: The UNIX date, in milliseconds, of the start of the subscription renewal period.
- `subscriptionEndDate` (subscriptionEndDate) *(required)*: The UNIX date, in milliseconds, of the end of the subscription renewal period.
- `subscriptionDaysOfPaidService` (subscriptionDaysOfPaidService) *(required)*: The total number of days of paid service for the subscription. For more information, see [`subscriptionDaysOfPaidService`](subscriptiondaysofpaidservice.md).
- `pricingCurrency` (pricingCurrency) *(required)*: The currency the transaction used to charge the customer. For more information, see [`pricingCurrency`](pricingcurrency.md).
- `reportingCurrency` (reportingCurrency) *(required)*: The currency you use to report all the amount fields, including `amountTaxExclusive`, `amountTaxInclusive`, `netAmountTaxExclusive`, and `taxAmount`. For  more information, see [`reportingCurrency`](reportingcurrency.md).
- `exchangeRate` (exchangeRate): The exchange rate you use to calculate the amounts, from the pricing currency to the reporting currency, if the customer is billed in an unsupported currency. For more information, see [`exchangeRate`](exchangerate.md).
- `amountTaxExclusive` (amountTaxExclusive) *(required)*: The amount that the customer paid, excluding taxes, that you state in milli-units of the reporting currency. For more information, see [`amountTaxExclusive`](amounttaxexclusive.md).
- `amountTaxInclusive` (amountTaxInclusive) *(required)*: The amount that the customer paid, including taxes, that you state in milli-units of the reporting currency. For more information, see [`amountTaxInclusive`](amounttaxinclusive.md).
- `netAmountTaxExclusive` (netAmountTaxExclusive) *(required)*: The net amount the customer was charged, accurate to the current line item, that you state in milli-units of the reporting currency. This amount excludes tax, and accounts for all refunds and restatements. For more information, see [`netAmountTaxExclusive`](netamounttaxexclusive.md).
- `taxAmount` (taxAmount) *(required)*: The amount the customer paid in taxes, that you state in milli-units of the reporting currency. For more information, see [`taxAmount`](taxamount.md).
- `taxCountry` (taxCountry) *(required)*: The country code of the country for which taxes were paid on the purchase. For more information, see [`taxCountry`](taxcountry.md).
- `productIdentifier` (productIdentifier) *(required)*: A string that uniquely identifies the subscription product.
- `quantity` (quantity) *(required)*: The quantity of the product the customer purchased. For more information, see [`quantity`](quantity.md).
- `eventType` (eventType) *(required)*: Use `BUY`. (To report a refund, use a [`RefundLineItem`](refundlineitem.md) line item instead.)
- `productType` (productType) *(required)*: Use `SUBSCRIPTION`. (To report a one-time charge transaction, use a [`OneTimeBuyLineItem`](onetimebuylineitem.md) instead.)

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/subscriptionbuylineitem)*