# Reporting corrections

**Framework**: External Purchase Server API

Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.

#### Overview

If you successfully submit a report to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint that you later find to be incorrect, you must correct your submission. To send a correction, fill out the [`ExternalPurchaseReport`](externalpurchasereport.md) request body with a new [`requestIdentifier`](requestidentifier.md) and the corrections, and call the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint. Send corrected reports promptly.

There are two types of corrections:

- A correction to transaction data in a line item. In this type of correction, you restate the entire line item with corrected data. Apple uses only the most recent submission for the line item.
- A retraction of a line item you previously sent. In this type of correction, you indicate that you erroneously sent the line item, and aren’t including the erroneously-submitted amounts in transaction calculations. Be sure to update the [`netAmountTaxExclusive`](netamounttaxexclusive.md) field so it represents the correct net amount, tax exclusive, of the transaction.

> ❗ **Important**: The [`netAmountTaxExclusive`](netamounttaxexclusive.md) must represent the correct net amount (excluding taxes) for the transaction, including in line items that are corrections.

##### Correct Data in a Line Item

To submit a line item with corrections, use the line item’s original [`lineItemId`](lineitemid.md) and include the [`restatement`](restatement.md) flag set to `true`. Make corrections to any type of line item: [`OneTimeBuyLineItem`](onetimebuylineitem.md), [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md), and [`RefundLineItem`](refundlineitem.md).

> ❗ **Important**: Restated line items overwrite the originally reported line item. Include all the data in the line item — even fields that are the same as the previous version.

Apple uses only the most recent version of the line item.

##### Retract an Erroneously Submitted Line Item

If you submitted a line item in error and want Apple to ignore it, use the same [`lineItemId`](lineitemid.md) as in the original submission. Set both the [`restatement`](restatement.md) and [`erroneouslySubmitted`](erroneouslysubmitted.md) fields to `true`. (You may undo this action by submitting the line item again, with [`restatement`](restatement.md) set to `true`, and [`erroneouslySubmitted`](erroneouslysubmitted.md) set to false.) Be sure to include all of the original line item data fields, and recalculate the [`netAmountTaxExclusive`](netamounttaxexclusive.md) field to correctly represent the net amount with the erroneously submitted line item accounted for.

Successfully submitting a line item with the `erroneouslySubmitted` flag is an effective “undo” of the original line item.

## See Also

- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/reportcorrections)*