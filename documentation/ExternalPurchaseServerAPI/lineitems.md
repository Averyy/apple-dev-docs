# Line item fields

**Framework**: External Purchase Server API

Properties that describe a single transaction or correction in an external purchase report.

## Topics

### Identifying the line item
- [type lineItemId](lineitemid.md)
  A unique identifier for the line item, that you determine.
### Providing transaction info
- [type creationDate](creationdate.md)
  The UNIX date, in milliseconds, that the customer authorized the transaction.
- [type eventType](eventtype.md)
  The type of transaction the line item reports, whether it’s a buy or refund.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.
### Providing product info
- [type productIdentifier](productidentifier.md)
  A string that identifies the product.
- [type productType](producttype.md)
  The type of product in the transaction, whether it’s a one-time buy, or a subscription.
- [type quantity](quantity.md)
  The quantity of the product the customer purchased in a single transaction.
### Specifying amounts and currency
- [type amountTaxExclusive](amounttaxexclusive.md)
  The amount, in milli-units, that the customer paid or was refunded, excluding taxes.
- [type amountTaxInclusive](amounttaxinclusive.md)
  The amount, in milli-units, that the customer paid, including taxes.
- [type netAmountTaxExclusive](netamounttaxexclusive.md)
  The net amount, in milli-units, that you charged the customer, pre-tax, and after deducting all refunds.
- [type taxAmount](taxamount.md)
  The amount, in milli-units, that the customer paid in taxes.
- [type taxCountry](taxcountry.md)
  The three-letter country code of the country that collects the taxes for the transaction.
- [type pricingCurrency](pricingcurrency.md)
  The currency used in the transaction to bill or refund the customer.
- [type reportingCurrency](reportingcurrency.md)
  The currency the line item uses to report all amount values.
- [type exchangeRate](exchangerate.md)
  A decimal value that is the exchange rate you use to convert the pricing currency to the reporting currency, when the two currencies differ.
### Supplying subscription info
- [type subscriptionDaysOfPaidService](subscriptiondaysofpaidservice.md)
  The total number of days of paid service for the subscription.
- [type subscriptionEndDate](subscriptionenddate.md)
  The UNIX date, in milli-seconds, the subscription renewal cycle ends.
- [type subscriptionEvent](subscriptionevent.md)
  The event in the subscription’s life cycle that the transaction represents.
- [type subscriptionStartDate](subscriptionstartdate.md)
  The UNIX date, in milli-seconds, of the start of the subscription renewal period.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.
### Submitting corrections
- [type erroneouslySubmitted](erroneouslysubmitted.md)
  A Boolean value that indicates whether a line item was submitted in error.
- [type restatement](restatement.md)
  A Boolean value that indicates a line item contains a correction.

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/lineitems)*